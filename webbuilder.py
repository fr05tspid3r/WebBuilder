import os
import shutil


source_directory = 'fr05tspi3r'

html_file_path = '/var/www/html/index.html'
css_file_path = '/var/www/html/styles.css'


if not os.path.exists(source_directory):
    print(f"Source directory '{source_directory}' does not exist.")
    exit(1)


if not os.path.isfile(os.path.join(source_directory, 'index.html')) or not os.path.isfile(os.path.join(source_directory, 'styles.css')):
    print("HTML and CSS files not found in the source directory.")
    exit(1)


source_html_timestamp = os.path.getmtime(os.path.join(source_directory, 'index.html'))
source_css_timestamp = os.path.getmtime(os.path.join(source_directory, 'styles.css'))

destination_html_timestamp = os.path.getmtime(html_file_path)
destination_css_timestamp = os.path.getmtime(css_file_path)


if (source_html_timestamp > destination_html_timestamp) or (source_css_timestamp > destination_css_timestamp):
    shutil.copy(os.path.join(source_directory, 'index.html'), html_file_path)
    shutil.copy(os.path.join(source_directory, 'styles.css'), css_file_path)

    os.system('sudo service apache2 start')

    os.system('google-chrome http://localhost')

    print("Webpage created and opened in Chrome. You can access it at http://localhost")
else:
    print("No changes detected in HTML and CSS files. Webpage not updated.")
