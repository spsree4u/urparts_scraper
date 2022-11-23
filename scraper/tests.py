
import pytest
from scraper.models import PartsDetails


@pytest.mark.django_db
def test_user_count():
    """Test DB access"""
    assert PartsDetails.objects.count() == 0
