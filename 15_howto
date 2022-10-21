
# how-to :: Responsive Web Design
---
## Overview
Responsive web design makes your webpages look good on screens of all sizes & aspect ratios.

### Estimated Time Cost: 0.6 hrs at home + 0.3 hrs at school = 0.9 hrs (round to nearest 0.1)

### Prerequisites:

- Basic CSS syntax (how to give styling properties to elements)
- Basic HTML syntax (how to create and organize webpages, and how to give attributes to elements)

1. Use relative units
    * **Definition**: units in CSS that are relative to the size of a different element, rather than absolute, like `px`)
	* `ch`
		* Relative to the width of the character “0”
		* *Example of use case:* If you’re using a monospaced font and want to make a `div` that is exactly 50 characters long, you could apply `width: 50em` to the `div`

	* `vw` and `vh`
		* Relative to the width and height of the visible area of the web page. Written as a number from 0 to 100
		* *Example of use case:* If you want to make a div that takes up the left half of the screen, regardless of screen size

	* `vmin` and `vmax`
		* `vmax` is relative to the <u>larger</u> dimension of the visible area of the web page (if the web page is wider than it is tall, then this is the width)
		* `vmin` is relative to the <u>smaller</u> dimension of the visible area of the web page (if the web page is wider than it is tall, then this is the height)
		* This is sometimes useful if your website will be used by both mobile users as well as desktop users, as the two platforms have different aspect ratios

	* `em`
		* Relative to the `font-size` of the element it's applied to

	* `rem`
		* Relative to the `font-size` of the root of the element it's applied to

2. Use flex items
	* **Definition**: flex items/flex elements are contained in a `<div>` (ex: `<div class="flex-container"> {STUFF} </div>`). These elements have a handful of properties responsive to window size:
    	* `order` -- defines the order in which flex elements are displayed
    	* `flex-grow` -- dictates how much an element grows **relative to other flex elements**
    	* `flex-shrink` -- dictates how much an element shrinks **relative to other flex elements**
    	* `flex-basis` -- defines the *initial size* of a `flex` element
    	* `flex` -- syntactic shortcut:
	    	* `flex: 0 0 30px` means the element does not grow, does not shrink, and is initially 30px long.
	    * `align-self` -- defines the elements alignment in a `flex` container

3. Use media queries
	* **Definition:** media queries allow you to include a block of CSS properties only if a certain set of conditions are true.
	
	* *Example:*
```css
@media only screen and (width <= 600px){
	body {
		background-color: lightblue;
	}
}
```
If the width is 600 px or smaller, then the styling will be applied, turning the background color of the screen to a light blue.


### Resources
* **[CSS units](https://www.w3schools.com/css/css_units.asp)**
* **[CSS flex](https://www.w3schools.com/cssref/css3_pr_flex.asp)**
* **[CSS flex-grow](https://www.w3schools.com/cssref/playdemo.asp?filename=playcss_flex-grow)**
* **[CSS media queries](https://www.w3schools.com/css/css_rwd_mediaqueries.asp)**

---

Accurate as of (last update): 2022-10-20

#### Contributors:  
Karen Shekyan, pd7  
Gabriel Thompson, pd7  
Russell Goychayev, pd7
