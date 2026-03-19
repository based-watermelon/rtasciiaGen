
# rtasciiaGen

### ASCII Art generator
##### Converts given Image into an Ascii art with adjustable scaliing factor

##### tutorial credit: Raphsonite
---

## Changes
<ol>
<li>Used Luminance-weighted grayscale instead of plain average</li>
<li>Smoother Char aspect ratio</li>
<li>Accounted for Alpha channel</li>
</ol>

## Setup
```bash
# clone the repo
git clone https://github.com/your-username/rtasciia.git
cd rtasciia

# create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# install dependencies
pip install pillow

# run
python rtasciiaGen/main.py
```

## Changing the image

Drop your image into the root `rtasciia/` folder, then open `rtasciiaGen/main.py` and change this line:
```python
img = Image.open("strawberry.png")  # replace with your filename
```
Supported Formats: PNG (recommended),JPEG,JPG

## Tweaking output

| Variable | What it does |
|---|---|
| `scale_factor` | Overall resolution of output |
| `char_aspect` | Adjust if output looks stretched/squished |
| `dense_gradient` | Swap for longer gradient for more detail (high to low density) |


