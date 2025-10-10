import pytest
from pages.faq_page import FaqPage

@pytest.mark.parametrize("idx", list(range(8))) 
def test_faq_answer_opens_and_has_text(driver, idx):
    faq = FaqPage(driver)
    faq.open_main()
    faq.expand_question(idx)
    text = faq.get_answer_text(idx)
    assert text, f"Ответ для вопроса {idx} пустой"

