import os
import numpy as np
from flask import Flask, render_template, request, flash, redirect, url_for, send_from_directory
from PIL import Image
from collections import defaultdict
from werkzeug.utils import secure_filename


class ColorAnalyzer:
    def __init__(self, image_path):
        self.image_path = image_path
        self.colors = None

    def analyze(self, num_colors=10, resize_to=400):
        """Analyze image colors with optional resizing for performance"""
        try:
            with Image.open(self.image_path) as img:
                # Convert and resize image
                img = img.convert('RGB').resize((resize_to, resize_to))
                pixels = np.array(img).reshape(-1, 3)

                # Use defaultdict for efficient counting
                color_counts = defaultdict(int)
                for pixel in pixels:
                    color_counts[tuple(pixel)] += 1

                # Get sorted colors by frequency
                sorted_colors = sorted(color_counts.items(),
                                       key=lambda x: x[1],
                                       reverse=True)[:num_colors]

                self.colors = [{
                    'hex': f'#{r:02x}{g:02x}{b:02x}',
                    'rgb': (r, g, b),
                    'count': count,
                    'percentage': (count / len(pixels)) * 100
                } for (r, g, b), count in sorted_colors]

            return True
        except Exception as e:
            print(f"Error analyzing image: {str(e)}")
            return False


app = Flask(__name__)
app.config.update({
    'UPLOAD_FOLDER': '/Users/sdasa/PycharmProjects/Extractcolors/static/img',
    'ALLOWED_EXTENSIONS': {'png', 'jpg', 'jpeg', 'gif'},
    'MAX_CONTENT_LENGTH': 5 * 1024 * 1024,  # 5MB limit
    'SECRET_KEY': os.urandom(24)
})


def validate_file(file):
    """Comprehensive file validation"""
    if not file:
        return False, "No file uploaded"
    if file.filename == '':
        return False, "Empty filename"
    if not allowed_file(file.filename):
        return False, "Invalid file type"
    return True, ""


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


@app.route('/', methods=['GET', 'POST'])
def handle_upload():
    if request.method == 'POST':
        file = request.files.get('file')

        # Validate file
        is_valid, message = validate_file(file)
        if not is_valid:
            flash(message, 'error')
            return redirect(url_for('handle_upload'))

        try:
            # Secure filename handling
            filename = secure_filename(file.filename)
            save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(save_path)

            # Analyze colors
            analyzer = ColorAnalyzer(save_path)
            if not analyzer.analyze():
                raise RuntimeError("Failed to analyze image colors")

            return render_template('index.html',
                                   filename=filename,
                                   colors=analyzer.colors)

        except Exception as e:
            flash(f"Processing error: {str(e)}", 'error')
            if os.path.exists(save_path):
                os.remove(save_path)
            return redirect(url_for('handle_upload'))

    return render_template('index.html')


@app.route('/image/<filename>')
def serve_image(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == '__main__':
    # Ensure upload folder exists
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)