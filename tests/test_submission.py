

from pathlib import Path

def test_index_html_exists():
    filename = "index.html"
    if not Path(filename).exists():
        print(f"❌ {filename} is missing")
        assert False, f"❌ {filename} is missing"
    else:
        print(f"✅ {filename} is present")
        assert True, f"✅ {filename} is present"

def test_about_html_exists():
    filename = "about.html"
    if not Path(filename).exists():
        print(f"❌ {filename} is missing")
        assert False, f"❌ {filename} is missing"
    else:
        print(f"✅ {filename} is present")
        assert True, f"✅ {filename} is present"

def test_cv_html_exists():
    filename = "cv.html"
    if not Path(filename).exists():
        print(f"❌ {filename} is missing")
        assert False, f"❌ {filename} is missing"
    else:
        print(f"✅ {filename} is present")
        assert True, f"✅ {filename} is present"

def test_gallery_html_exists():
    filename = "gallery.html"
    if not Path(filename).exists():
        print(f"❌ {filename} is missing")
        assert False, f"❌ {filename} is missing"
    else:
        print(f"✅ {filename} is present")
        assert True, f"✅ {filename} is present"

def test_contact_html_exists():
    filename = "contact.html"
    if not Path(filename).exists():
        print(f"❌ {filename} is missing")
        assert False, f"❌ {filename} is missing"
    else:
        print(f"✅ {filename} is present")
        assert True, f"✅ {filename} is present"

def test_style_css_exists():
    filename = "css/style.css"
    if not Path(filename).exists():
        print(f"❌ {filename} is missing")
        assert False, f"❌ {filename} is missing"
    else:
        print(f"✅ {filename} is present")
        assert True, f"✅ {filename} is present"

def test_documentation_pdf_exists():
    filename = "Documentation.pdf"
    if not Path(filename).exists():
        print(f"❌ {filename} is missing")
        assert False, f"❌ {filename} is missing"
    else:
        print(f"✅ {filename} is present")
        assert True, f"✅ {filename} is present"

def test_images_dir_exists():
    filename = "images/"
    if not Path(filename).exists():
        print(f"❌ {filename} is missing")
        assert False, f"❌ {filename} is missing"
    else:
        print(f"✅ {filename} is present")
        assert True, f"✅ {filename} is present"

def test_css_dir_exists():
    filename = "css/"
    if not Path(filename).exists():
        print(f"❌ {filename} is missing")
        assert False, f"❌ {filename} is missing"
    else:
        print(f"✅ {filename} is present")
        assert True, f"✅ {filename} is present"


# Test for at least 10 image files in the images directory
def test_at_least_10_images_exist():
    images_dir = Path("images/")
    if not images_dir.exists() or not images_dir.is_dir():
        print("❌ images/ directory is missing or not a directory")
        assert False, "❌ images/ directory is missing or not a directory"
    # Count files with common image extensions
    image_extensions = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".tiff", ".svg"}
    image_files = [f for f in images_dir.iterdir() if f.is_file() and f.suffix.lower() in image_extensions]
    print(f"Found {len(image_files)} image files in images/: {[f.name for f in image_files]}")
    if len(image_files) < 10:
        print(f"❌ Less than 10 image files found in images/ (found {len(image_files)})")
        assert False, f"❌ Less than 10 image files found in images/ (found {len(image_files)})"
    else:
        assert True, f"✅ At least 10 image files are present in images/"
        print("✅ At least 10 image files are present in images/")


