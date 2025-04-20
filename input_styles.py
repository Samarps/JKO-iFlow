# Dynamically extracts all the input styles
# from the available images like img_rose.png, img_tree.png, etc
# and stores the input styles in input_styles.yaml

import os
import yaml

style_images = [f for f in os.listdir('.') if f.startswith('img_') and f.endswith('.png')]

styles = [f[4:-4] for f in style_images]

with open('input_styles.yaml', 'w') as f:
    f.write('\n'.join(styles))

print("Extracted styles:", styles)