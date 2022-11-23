

from scraper.utils.scraper_utils import Scraper
from scraper.utils.db_utils import DBUtil
from scraper.config import BASE_URL


def scraping(url, property_map):
    print(f"Scraping {url}")
    sc = Scraper(url)
    data = sc.get_data_list(property_map)
    return data


def load_data():
    db = DBUtil()

    companies = scraping(BASE_URL, {"class": "c_container allmakes"})

    record_id = 0
    for company in companies:

        company_url = BASE_URL + "{0}".format(company)

        categories = scraping(company_url,
                              {"class": "c_container allmakes allcategories"})

        for category in categories:
            category_url = company_url + "/{0}".format(
                category.replace(' ', '%20'))

            part_models = scraping(category_url,
                                   {"class": "c_container allmodels"})

            for part_model in part_models:
                model_url = category_url + "/{0}".format(
                    part_model.replace(' ', '%20'))

                sections = scraping(model_url,
                                    {"class": "c_container modelSections"})
                if sections:
                    for section in sections:
                        section_url = model_url + "/{0}".format(
                            section.replace(' ', '%20'))
                        parts = scraping(section_url,
                                         {"class": "c_container allparts"})
                        for part in parts:
                            record_id = record_id + 1
                            print(record_id)
                            db.save_to_db(
                                'parts_details',
                                [record_id, company, category,
                                 part_model, part],
                                ['id', 'company_name', 'category_name',
                                 'model_name', 'part_name'])
                else:
                    parts = scraping(model_url,
                                     {"class": "c_container allparts"})

                    for part in parts:
                        record_id = record_id + 1
                        # print(record_id)
                        print([record_id, company, category,
                                              part_model, part])
                        db.save_to_db(
                            'parts_details',
                            [record_id, company, category, part_model, part],
                            ['id', 'company_name', 'category_name',
                             'model_name', 'part_name'])

    db.close_db_connection()


if __name__ == '__main__':
    load_data()
