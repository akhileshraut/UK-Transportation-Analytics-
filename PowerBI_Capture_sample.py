from playwright.sync_api import sync_playwright
import time
import os

# POWER BI REPORT URL

POWER_BI_URL = input(
    "Paste Power BI report URL: "
).strip()

# OUTPUT FOLDER

OUTPUT_FOLDER = r"D:\PowerBI_Export"

os.makedirs(
    OUTPUT_FOLDER,
    exist_ok=True
)

print("\nImages will be saved here:")
print(OUTPUT_FOLDER)

# FILE NAMES

file_names = [
    "01_Punctuality_Overview.png",
    "02_Mode_Delay_Analysis.png",
    "03_Area_Deep_Dive.png",
    "04_Top_100_Delay_Investigation.png",
    "05_EV_Charging_Infrastructure.png"
]

# START PLAYWRIGHT

with sync_playwright() as p:

    browser = p.chromium.launch(
        headless=False
    )

    page = browser.new_page(
        viewport={
            "width": 1920,
            "height": 1080
        },
        device_scale_factor=2
    )
    
    # OPEN POWER BI REPORT
    
    print("\nOpening Power BI report...")

    page.goto(
        POWER_BI_URL,
        wait_until="domcontentloaded"
    )

    print("Waiting for Power BI to load...")

    time.sleep(15)
    
    # PAGE 1
    
    print("\n" + "=" * 60)
    print("Capturing Page 1")
    print("=" * 60)

    path = os.path.join(
        OUTPUT_FOLDER,
        file_names[0]
    )

    page.screenshot(
        path=path,
        full_page=False
    )

    print("Saved:")
    print(path)
    
    # FIND NEXT PAGE BUTTON
    
    next_button = page.locator(
        '[aria-label="Next Page"]'
    )

    print(
        "\nNext Page buttons found:",
        next_button.count()
    )
    
    # MOVE THROUGH PAGES 2 TO 5
    
    for page_number in range(2, 6):

        print("\n" + "=" * 60)

        print(
            f"Moving to Page {page_number}"
        )

        print("=" * 60)


        try:

            # Find Next Page button again

            next_button = page.locator(
                '[aria-label="Next Page"]'
            )

            count = next_button.count()

            print(
                "Next Page buttons found:",
                count
            )


            if count == 0:

                print(
                    "ERROR: Next Page button not found."
                )

                break


            # Click Next Page

            print(
                "Clicking Next Page..."
            )

            next_button.last.click(
                force=True
            )

            print(
                "Next Page clicked."
            )


            # WAIT FOR PAGE TO CHANGE

            print(
                "\nWaiting 30 seconds for "
                "Power BI visuals to render..."
                )

            time.sleep(30)

            # SCREENSHOT

            path = os.path.join(
                OUTPUT_FOLDER,
                file_names[page_number - 1]
            )

            print(
                "Taking screenshot..."
            )

            page.screenshot(
                path=path,
                full_page=False
            )

            print(
                "Saved:"
            )

            print(path)


        except Exception as e:

            print(
                "\nERROR while processing Page",
                page_number
            )

            print(e)

            break
    
    # FINAL FILE CHECK 

    print("\n")
    print("=" * 60)
    print("FILES CREATED")
    print("=" * 60)

    files = os.listdir(
        OUTPUT_FOLDER
    )

    if len(files) == 0:

        print(
            "No files were created."
        )

    else:

        for file in files:

            full_path = os.path.join(
                OUTPUT_FOLDER,
                file
            )

            print(
                full_path
            )
    
    # OPEN OUTPUT FOLDER

    print("\nOpening output folder...")

    os.startfile(
        OUTPUT_FOLDER
    )
    
    # KEEP BROWSER OPEN
    
    input(
        "\nPress Enter to close the browser..."
    )

    browser.close()
    