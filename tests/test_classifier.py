from unittest.mock import MagicMock, patch

import pytest
from pydantic import ValidationError

from app.classifier import classify_email
from app.schemas import EmailCategory


def test_billing_classification():
    mock_response = MagicMock()

    mock_response.message.content = (
        '{"category": "billing", '
        '"summary": "Customer requests a refund."}'
    )

    with patch("app.classifier.Client") as mock_client:
        mock_client.return_value.chat.return_value = mock_response

        result = classify_email(
            "I was charged twice for my subscription."
        )

    assert result.category == EmailCategory.BILLING
    assert result.summary == "Customer requests a refund."


def test_empty_email():
    with pytest.raises(ValueError):
        classify_email("")


def test_invalid_llm_category():
    mock_response = MagicMock()

    mock_response.message.content = (
        '{"category": "unknown", '
        '"summary": "Customer has a problem."}'
    )

    with patch("app.classifier.Client") as mock_client:
        mock_client.return_value.chat.return_value = mock_response

        with pytest.raises(ValidationError):
            classify_email("I need help with my account.")