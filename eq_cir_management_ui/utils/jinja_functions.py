from typing import List, Optional


def create_error_panel_data(
    form_errors: dict[str, List[str | List[str]]], parent_string="", error_order=[]
) -> [dict[str:str]]:
    field_errors = []

    # Order errors to match the optional expected order
    error_process_order = []
    if error_order:
        for form_error_key in error_order:
            if form_error_key in form_errors.keys():
                form_error_item = {form_error_key: form_errors[form_error_key]}
                error_process_order.append(form_error_item)
    else:
        for k, v in form_errors.items():
            error_process_order.append({k: v})

    for form_error in error_process_order:
        field = list(form_error.keys())[0]
        error_obj = form_error[field]
        if isinstance(error_obj, list):
            error_list = error_obj
            if not error_list:
                continue
            if isinstance(error_list[0], str):
                url = (
                    f"#{parent_string}-{field}_error"
                    if parent_string
                    else f"#{field}_error"
                )
                field_errors.append({"url": url, "text": error_list[0]})
            elif isinstance(error_list[0], list):
                for index, sublist in enumerate(error_list, 1):
                    if sublist and sublist[0]:
                        field_errors.append(
                            {"url": f"#{field}-{index}_error", "text": sublist[0]}
                        )
        if isinstance(error_obj, dict):
            new_field_errors = create_error_panel_data(error_obj, field)
            field_errors = field_errors + new_field_errors

    return field_errors


def create_ordered_error_panel_data(form_errors, error_order):
    ordered_errors = []
    error_panel_data = create_error_panel_data(form_errors=form_errors)
    for field_url in error_order:
        for field_error in error_panel_data:
            if field_error.get("url") == field_url:
                ordered_errors.append(field_error)

    return ordered_errors


def get_field_error(field_id: str, form_errors: dict) -> Optional[dict]:
    """Builds a design system compliant error dict from a wtf-forms errors
    dict. Returns None if no errors were produced.

    :param field_id: ID of the field the error should be applied to.
    :param form_errors: A dict of form errors from wtf-forms.
    :return: Design System compliant error dict.
    """
    if type(form_errors) is dict:
        if "-" in field_id:
            error_key = field_id.split("-")[0]
            sub_error_key = field_id.split("-")[1]

            error_list = form_errors.get(error_key)
            if error_list:
                error_sublist = error_list.get(sub_error_key)
                if error_sublist:
                    return {"id": f"{field_id}_error", "text": error_sublist[0]}
        else:
            errors = form_errors.get(field_id)
            if errors:
                return {"id": f"{field_id}_error", "text": errors[0]}
    else:
        errors = form_errors.get(field_id)
        if errors:
            return {"id": f"{field_id}_error", "text": errors[0]}

    return None
