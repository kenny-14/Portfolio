import flet as ft
import os
import sys
import subprocess


def main(page: ft.Page):
    page.title = "Kenny - Engineering Portfolio"
    page.theme_mode = "dark"
    page.bgcolor = "#111111"
    page.scroll = "auto"
    page.padding = 0
    page.spacing = 0

    # ---------------- FIXED PDF OPENER ----------------
    def close_dialog(e):
        page.dialog.open = False
        page.update()

    def open_file(filename, file_type="File"):
        app_folder = os.path.dirname(os.path.abspath(__file__))
        desktop = os.path.join(os.path.expanduser("~"), "Desktop")
        onedrive_desktop = os.path.join(os.path.expanduser("~"), "OneDrive", "Desktop")

        # Some files were saved as ".pdf.pdf", so try both names.
        filenames_to_try = [filename]
        if filename.lower().endswith(".pdf"):
            filenames_to_try.append(filename + ".pdf")

        folders_to_try = [
            app_folder,
            os.getcwd(),
            os.path.join(desktop, "Kenny Codes"),
            os.path.join(onedrive_desktop, "Kenny Codes"),
            desktop,
            onedrive_desktop,
        ]

        paths_to_try = [
            os.path.join(folder, pdf_name)
            for folder in folders_to_try
            for pdf_name in filenames_to_try
        ]

        found_path = None
        for path in paths_to_try:
            if os.path.exists(path):
                found_path = path
                break

        if found_path:
            try:
                if sys.platform == "win32":
                    os.startfile(found_path)
                elif sys.platform == "darwin":
                    subprocess.Popen(["open", found_path])
                else:
                    subprocess.Popen(["xdg-open", found_path])
                return  # Success
            except Exception as ex:
                msg = f"File found but couldn't open it.\n\nError: {ex}"
        else:
            searched = "\n".join(f"  {p}" for p in paths_to_try)
            msg = (
                f"{file_type} not found: {filename}\n\n"
                f"Searched in:\n{searched}\n\n"
                f"Fix: Put the file in the same folder as kenny.py."
            )

        page.dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text(f"{file_type} Error", color="white"),
            content=ft.Text(msg, color="#B0B0B0"),
            actions=[ft.TextButton("Close", on_click=close_dialog)],
        )
        page.dialog.open = True
        page.update()

    def open_pdf(filename):
        open_file(filename, "PDF")

    # --- KEY FIX: default argument trick stops lambda capture-by-reference bug ---
    def cert_button(label, filename):
        def handle_click(e, f=filename):
            open_pdf(f)
        return ft.TextButton(
            content=ft.Text(label, color="#4caf50", size=15),
            on_click=handle_click,
        )

    def video_button(label, filename):
        def handle_click(e, f=filename):
            open_file(f, "Video")
        return ft.TextButton(
            content=ft.Text(label, color="#4caf50", size=15),
            on_click=handle_click,
        )

    # ---------------- DYNAMIC CONTENT CONTAINER ----------------
    content_area = ft.Column()

    def show_section(section_control):
        content_area.controls.clear()
        content_area.controls.append(section_control)
        page.update()

    # ---------------- PORTFOLIO DATA SECTIONS ----------------
    timeline = ft.Column([
        ft.Text("📅 Project Timeline", size=24, weight="bold", color="white"),
        ft.Text("• Week 1: Project planning and initial idea contribution", size=16, color="#B0B0B0"),
        ft.Text("• Week 2: UI layout configuration and initial Flet setup", size=16, color="#B0B0B0"),
        ft.Text("• Week 3: Functional feature engineering and implementation", size=16, color="#B0B0B0"),
        ft.Text("• Week 4: Rigid software testing, code validation, and debugging", size=16, color="#B0B0B0"),
        ft.Text("• Week 5: Live application deployment and documentation", size=16, color="#B0B0B0"),
    ], spacing=12)

    matlab = ft.Column([
        ft.Text("🎓 MATLAB Achievement Hub", size=24, weight="bold", color="white"),
        ft.Text("Verified MathWorks Course Certifications:", size=16, weight="bold", color="#888888"),
        ft.Text("Click a green certificate below to open the PDF:", size=14, color="#B0B0B0"),
        ft.Text(""),

        cert_button("1. 📄 View MATLAB Onramp Certificate",            "matlab_onramp.pdf"),
        cert_button("2. 📄 View Simulink Onramp Certificate",          "simulink_onramp.pdf"),
        cert_button("3. 📄 View Signal Processing Onramp Certificate", "signal_onramp.pdf"),
        cert_button("4. 📄 View Control Systems Onramp Certificate",   "controls_onramp.pdf"),
        cert_button("5. 📄 View Image Processing Onramp Certificate",  "image_onramp.pdf"),

        ft.TextButton(content=ft.Text("6. 🏆 Machine Learning Onramp (Coming Soon)", color="#555555", size=15)),
        ft.TextButton(content=ft.Text("7. 🏆 Deep Learning Onramp (Coming Soon)",    color="#555555", size=15)),
        ft.TextButton(content=ft.Text("8. 🏆 MATLAB Fundamentals (Coming Soon)",     color="#555555", size=15)),

        ft.Text(""),
        ft.Text(
            "💡 Tip: PDFs must be inside your Desktop → Kenny Codes folder.",
            size=12, italic=True, color="#555555"
        ),
    ], spacing=4)

    blog = ft.Column([
        ft.Text("📝 Technical Blog - Confidence in Concepts", size=24, weight="bold", color="white"),
        cert_button("📄 View ICR PDF", "ICR_Chomore_K_updated.pdf"),
        ft.Text("Ball Mill Site Visit — How Load IQ Was Born", size=18, weight="bold", color="white"),
        video_button("▶ Open Site Visit Video", "WhatsApp Video 2026-06-01 at 12.50.37 AM.mp4"),
    ], spacing=12)

    github = ft.Column([
        ft.Text("💻 GitHub Evidence & Contribution Logs", size=24, weight="bold", color="white"),
        ft.Text("📌 Commit History & Documentation:", size=18, weight="bold", color="#888888"),
        ft.Text(
            "Individual repository impact logs and feature deployment verification tracking.",
            size=15, color="#B0B0B0"
        ),
    ], spacing=12)

    # ---------------- NAVIGATION BUTTONS (same fix applied) ----------------
    def nav_btn(label, section):
        def handle(e, s=section):
            show_section(s)
        return ft.ElevatedButton(label, on_click=handle, bgcolor="#333333", color="white")

    nav_buttons = ft.Row([
        nav_btn("Timeline",   timeline),
        nav_btn("MATLAB Hub", matlab),
        nav_btn("Blog",       blog),
        nav_btn("GitHub",     github),
    ], spacing=12)

    # ---------------- HERO SECTION ----------------
    hero_section = ft.Container(
        content=ft.Row([
            ft.Column([
                ft.Text("Hi, I'm Kenny", size=22, color="white", weight="bold"),
                ft.Text("Mechanical\nEngineering", size=50, weight="bold", color="white", height=150),
                ft.Text(
                    "Mechanical Engineering Student specializing in structural calculations, "
                    "computed optimization modeling, and core programming paradigms.",
                    size=16, color="#888888", width=420
                ),
                ft.Text(""),
                nav_buttons,
            ], spacing=5),

            ft.VerticalDivider(expand=True, color="transparent"),

            ft.Container(
                width=320,
                height=320,
                bgcolor="#222222",
                border_radius=160,
                clip_behavior=ft.ClipBehavior.HARD_EDGE,
                content=ft.Image(
                    src="web.photo.jpeg.jpeg",
                    fit="cover",
                    width=320,
                    height=320,
                ),
            ),
        ]),
        padding=60,
        height=480,
    )

    show_section(timeline)

    page.add(
        ft.Container(
            content=ft.Column(
                [
                    hero_section,
                    ft.Container(content=content_area, padding=60),
                ],
                spacing=0,
            ),
            image=ft.DecorationImage(
                src="resource.jpg",
                fit=ft.BoxFit.COVER,
                opacity=0.35,
            ),
            bgcolor="#111111",
            expand=True,
        )
    )


ft.app(target=main, assets_dir="assets")
