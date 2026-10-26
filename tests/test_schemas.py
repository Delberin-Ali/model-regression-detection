import pytest

from pydantic import ValidationError

from app.schemas import EmailCategory, EmailClassification

def test_valid_classfication():
    result = EmailClassification(
        category="billing",
        summary="Customers reports a duplicate charde."
    )
    assert result.category == EmailCategory.BILLING


def test_invalid_category():
    with pytest.raises(ValidationError):
        EmailClassification(
            category="Unknown",
            summary=" Customers has a problem."
        )


def test_empty_summary():
    with pytest.raises(ValidationError):
        EmailClassification(
            category="billing",
            summary=""
        )