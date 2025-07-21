from faker import Faker

from config import setting


fake = Faker()

def fill_check_out_form_with_random_person_info(page_with_delivery_form):
    first_name = fake.first_name()
    last_name = fake.last_name()
    postal_code = fake.postalcode()
    page_with_delivery_form.fill_first_name(first_name)
    page_with_delivery_form.check_first_name_field_is_filled_with_text(first_name)
    page_with_delivery_form.fill_last_name(last_name)
    page_with_delivery_form.check_last_name_field_is_filled_with_text(last_name)
    page_with_delivery_form.fill_postal_code(postal_code)
    page_with_delivery_form.check_postal_code_field_is_filled_with_text(postal_code)