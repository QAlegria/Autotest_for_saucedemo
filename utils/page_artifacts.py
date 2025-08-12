import allure


def save_page_artifacts(page):
    for idx, p in enumerate(page.context.pages, start=1):
        try:
            p.bring_to_front()
            screenshot = p.screenshot(full_page=True)
            allure.attach(
                screenshot,
                name=f"Screenshot tab {idx}",
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            allure.attach(
                str(e),
                name=f"Screenshot tab {idx} FAILED",
                attachment_type=allure.attachment_type.TEXT
            )

        try:
            html = p.content()
            allure.attach(
                html,
                name=f"HTML tab {idx}",
                attachment_type=allure.attachment_type.HTML
            )
        except Exception as e:
            allure.attach(
                str(e),
                name=f"HTML tab {idx} FAILED",
                attachment_type=allure.attachment_type.TEXT
            )