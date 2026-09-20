from playwright.sync_api import sync_playwright
import time
import os


# ============================================================
# POWER BI REPORT URL
# ============================================================

POWER_BI_URL = input(
    "Paste Power BI report URL: "
).strip()


# ============================================================
# OUTPUT FOLDER
# ============================================================

OUTPUT_FOLDER = r"D:\PowerBI_Export"

os.makedirs(
    OUTPUT_FOLDER,
    exist_ok=True
)

print("\nImages will be saved here:")
print(OUTPUT_FOLDER)


# ============================================================
# WAIT FOR POWER BI / ZOOMCHARTS
# ============================================================

def wait_for_visuals(page, page_number):

    print("\n" + "-" * 60)
    print(f"Preparing Page {page_number}")
    print("-" * 60)

    print(
        "Waiting 15 seconds for Power BI / ZoomCharts..."
    )

    time.sleep(15)

    # Trigger rendering
    try:

        page.evaluate("""
            () => {
                window.scrollTo(0, 0);
                window.dispatchEvent(
                    new Event('resize')
                );
            }
        """)

        time.sleep(2)

        page.evaluate("""
            () => {
                window.scrollTo(
                    0,
                    document.body.scrollHeight
                );
            }
        """)

        time.sleep(2)

        page.evaluate("""
            () => {
                window.scrollTo(0, 0);
            }
        """)

        time.sleep(2)

        page.evaluate("""
            () => {
                window.dispatchEvent(
                    new Event('resize')
                );
            }
        """)

        time.sleep(3)

    except Exception as e:

        print(
            "Rendering warning:",
            e
        )

    print(
        f"Page {page_number} ready."
    )


# ============================================================
# GET REPORT STATE
# ============================================================

def get_report_state(page):

    try:

        return page.evaluate("""
            () => {

                // Get visible text from the Power BI report
                const bodyText =
                    document.body.innerText || "";

                // Get aria labels
                const ariaElements =
                    Array.from(
                        document.querySelectorAll(
                            '[aria-label]'
                        )
                    )
                    .map(
                        el =>
                            el.getAttribute(
                                'aria-label'
                            )
                    )
                    .filter(Boolean)
                    .join('|');

                // Get visible SVG/canvas count
                const svgCount =
                    document.querySelectorAll(
                        'svg'
                    ).length;

                const canvasCount =
                    document.querySelectorAll(
                        'canvas'
                    ).length;

                return (
                    bodyText.substring(0, 15000)
                    + "||ARIA||"
                    + ariaElements
                    + "||SVG||"
                    + svgCount
                    + "||CANVAS||"
                    + canvasCount
                );
            }
        """)

    except Exception:

        return ""


# ============================================================
# START PLAYWRIGHT
# ============================================================

with sync_playwright() as p:

    browser = p.chromium.launch(

        headless=False,

        args=[
            "--disable-blink-features=AutomationControlled",
            "--enable-gpu",
            "--ignore-gpu-blocklist",
            "--enable-webgl",
            "--use-gl=desktop",
            "--disable-dev-shm-usage"
        ]
    )


    # ========================================================
    # BROWSER PAGE
    # ========================================================

    page = browser.new_page(

        viewport={
            "width": 1920,
            "height": 1080
        },

        device_scale_factor=2
    )


    # ========================================================
    # OPEN POWER BI
    # ========================================================

    print(
        "\nOpening Power BI report..."
    )

    page.goto(
        POWER_BI_URL,
        wait_until="domcontentloaded",
        timeout=120000
    )


    # ========================================================
    # INITIAL LOAD
    # ========================================================

    print(
        "\nWaiting 15 seconds for Power BI..."
    )

    time.sleep(15)


    # ========================================================
    # PAGE COUNTER
    # ========================================================

    page_number = 1


    # ========================================================
    # MAIN LOOP
    # ========================================================

    while True:

        print("\n")
        print("=" * 60)
        print(
            f"PROCESSING PAGE {page_number}"
        )
        print("=" * 60)


        # ----------------------------------------------------
        # WAIT FOR VISUALS
        # ----------------------------------------------------

        wait_for_visuals(
            page,
            page_number
        )


        # ----------------------------------------------------
        # TAKE SCREENSHOT
        # ----------------------------------------------------

        file_name = (
            f"Page_{page_number:02d}.png"
        )

        screenshot_path = os.path.join(
            OUTPUT_FOLDER,
            file_name
        )


        print(
            "\nTaking screenshot..."
        )


        page.screenshot(

            path=screenshot_path,

            full_page=False,

            animations="disabled"
        )


        print(
            "Saved:"
        )

        print(
            screenshot_path
        )


        # ====================================================
        # GET CURRENT PAGE STATE
        # ====================================================

        old_state = get_report_state(
            page
        )


        # ====================================================
        # FIND NEXT PAGE
        # ====================================================

        next_button = page.locator(
            '[aria-label="Next Page"]'
        )

        count = next_button.count()


        print(
            "\nNext Page buttons found:",
            count
        )


        # ----------------------------------------------------
        # NO BUTTON
        # ----------------------------------------------------

        if count == 0:

            print(
                "\nNo Next Page button found."
            )

            print(
                "Reached final page."
            )

            break


        button = next_button.last


        # ----------------------------------------------------
        # CHECK BUTTON
        # ----------------------------------------------------

        try:

            if not button.is_visible():

                print(
                    "\nNext Page is not visible."
                )

                print(
                    "Reached final page."
                )

                break

        except Exception:

            break


        # ====================================================
        # CLICK NEXT PAGE
        # ====================================================

        print(
            f"\nClicking Next Page..."
        )


        try:

            button.click(
                force=True
            )

        except Exception as e:

            print(
                "\nCould not click Next Page:"
            )

            print(e)

            break


        # ====================================================
        # WAIT FOR PAGE TRANSITION
        # ====================================================

        print(
            "\nWaiting 5 seconds for "
            "Power BI page transition..."
        )

        time.sleep(5)


        # ====================================================
        # CHECK WHETHER PAGE CHANGED
        # ====================================================

        print(
            "Checking whether the report page changed..."
        )


        new_state = get_report_state(
            page
        )


        # ====================================================
        # PAGE DID NOT CHANGE
        # ====================================================

        if (
            old_state
            and new_state
            and old_state == new_state
        ):

            print("\n" + "=" * 60)

            print(
                "PAGE DID NOT CHANGE"
            )

            print("=" * 60)

            print(
                "The report is already on the last page."
            )

            print(
                "Stopping screenshot process."
            )

            # Remove the page that would have
            # otherwise been captured
            next_file = os.path.join(
                OUTPUT_FOLDER,
                f"Page_{page_number + 1:02d}.png"
            )

            if os.path.exists(next_file):

                os.remove(
                    next_file
                )

            break


        # ====================================================
        # PAGE CHANGED
        # ====================================================

        print(
            "\nPage changed successfully."
        )

        page_number += 1


    # ========================================================
    # FINAL FILE CHECK
    # ========================================================

    print("\n")
    print("=" * 60)
    print("FILES CREATED")
    print("=" * 60)


    image_files = [

        file

        for file in os.listdir(
            OUTPUT_FOLDER
        )

        if file.lower().endswith(
            (".png", ".jpg", ".jpeg")
        )
    ]


    image_files.sort()


    for file in image_files:

        print(
            os.path.join(
                OUTPUT_FOLDER,
                file
            )
        )


    print(
        "\nTotal pages captured:",
        len(image_files)
    )


    # ========================================================
    # OPEN OUTPUT FOLDER
    # ========================================================

    os.startfile(
        OUTPUT_FOLDER
    )


    # ========================================================
    # KEEP BROWSER OPEN
    # ========================================================

    input(
        "\nPress Enter to close browser..."
    )


    browser.close()