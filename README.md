# Heritage Company

Welcome to the Readme file for Heritage Company, a e-commerce site selling luxury timepieces. Built with [Django](https://www.djangoproject.com/).

![Site Screenshot across multiple devices](static/assets/images/readme-images/site-mockups.jpg)

<br>

- **[Link to Live Site](https://heritage-company.net)**

- [Link to Github Project Board](https://github.com/users/leonp84/projects/4)

<br>
<hr>

# Table of Contents

- [Overview](#overview)
- [UX](#ux)
  - [User Stories](#user-stories)
  - [Site Administrator](#site-administrator)
- [Business Model](#business-model)
  - [Luxury Watches – The Philosophy](#luxury-watches--the-philosophy)
  - [Heritage Company – The Story](#heritage-company--the-story)
- [Marketing Strategy](#marketing-strategy)
  - [Future Marketing Ideas](#future-marketing-ideas)
- [SEO](#seo)
  - [Google Search Console](#google-search-console)
- [Site Design](#site-design)
  - [Visuals](#visuals)
  - [Logo](#logo)
  - [Wireframing](#wireframing)
  - [Flowchart](#flowchart)
  - [Model Design and Relationships](#model-design-and-relationships)
- [Features](#features)
  - [Landing Page](#landing-page)
  - [Header](#header)
  - [Footer](#footer)
  - [Newsletter Sign-up](#newsletter-sign-up)
  - [All Products](#all-products)
  - [Brand Specific Pages](#brand-specific-pages)
  - [Discounted Products](#discounted-products)
  - [Product Search](#product-search)
  - [Advanced Search](#advanced-search)
  - [Product Details Page](#product-details-page)
  - [Product Contact](#product-contact)
  - [Accounts: Sign-up and Login](#accounts-sign-up-and-login)
  - [Accounts: Profile Page](#accounts-profile-page)
  - [Wish List](#wish-list)
  - [Past Orders](#past-orders)
  - [Shopping Bag](#shopping-bag)
  - [Checkout](#checkout)
  - [Create Account upon checkout](#create-account-upon-checkout)
  - [Order Payment](#order-payment)
  - [Order Confirmation](#order-confirmation)
  - [Superuser Functionality](#superuser-functionality)
  - [Superuser Statistics](#superuser-statistics)
  - [Miscellaneous Pages](#miscellaneous-pages)
- [Testing](#testing)
  - [Manual Testing](#manual-testing)
  - [Automated Testing](#automated-testing)
  - [Validator Testing](#validator-testing)
- [Bugs](#bugs)
- [Deployment](#deployment)
- [Links](#links)
- [Credits](#credits)

# Overview

Heritage Company is a fully operative e-commerce platform selling luxury watches from the well-known Swiss brands _Breitling_, _Tag Heuer_, _Omega_ and _Tissot_. Customers can browse products and make purchases through a functioning checkout and payment system that includes email verification. The site and product display have been carefully designed to be visually appealing to the targeted demographic.

# UX

## User Stories

### User

All User Story cards can be viewed on the [Github Project Board](https://github.com/users/leonp84/projects/4)

<hr>

1. **[EPIC 1: View and Navigation](https://github.com/leonp84/code-institute-project-5/issues/1)** - A set of features that allow users to view store products as listings, and then view each product in detail, with accompanying images.
<br>
<details>
<summary> User Stories for Epic: View and Navigation</summary>
<br>

> [#2](https://github.com/leonp84/code-institute-project-5/issues/2) - As a **site user** I can **view the list of available watches** so that I **can browse the story and make decisions** regarding purchases.

> [#3](https://github.com/leonp84/code-institute-project-5/issues/3) - As a **site user** I can **view the details of an individual product** so that I can **learn more about the watch before making a purchase**.

> [#4](https://github.com/leonp84/code-institute-project-5/issues/4) - As a **site user** I can **view multiple images of a product** so that I can **see the watch from different angles and make a better purchasing decision**.

> [#5](https://github.com/leonp84/code-institute-project-5/issues/5) - As a **site user** I can **see the number of items in my shopping cart** so that I can **keep track of my selected products**.

</details>
<hr>

2. **[EPIC 2: General Site Functionality](https://github.com/leonp84/code-institute-project-5/issues/6)** - A set of features that allow users to view non product related pages on the site, contact site owners, and sign up for newsletters.
<br>
<details>
<summary> User Stories for Epic: General Site Functionality</summary>
<br>

> [#7](https://github.com/leonp84/code-institute-project-5/issues/7) - As a **site user** I can **view an About Me page with an FAQ section** so that I can **learn more about the business and find answers to common questions**.

> [#8](https://github.com/leonp84/code-institute-project-5/issues/8) - As a **site user** I can **see a list of discounted items** so that I can **find luxury watches on sale and make cost-effective purchases**.

> [#9](https://github.com/leonp84/code-institute-project-5/issues/9) - As a **site user** I can **view the privacy statement and terms of service** so that I can **understand how my data will be used and the legal terms of using the site**.

> [#10](https://github.com/leonp84/code-institute-project-5/issues/10) - As a **site user** I can **sign up for the newsletter** so that I can **receive updates and promotional offers**.

> [#11](https://github.com/leonp84/code-institute-project-5/issues/11) - As a **site user** I can **receive a discount code upon signing up for the newsletter** so that I can **enjoy savings on my first purchase**.

> [#12](https://github.com/leonp84/code-institute-project-5/issues/12) - As a **site user** I can **contact the business with product-specific questions** so that I can **get more information and make informed purchase decisions**.

</details>
<hr>

3. **[EPIC 3: User Account Management](https://github.com/leonp84/code-institute-project-5/issues/13)** - A set of features that allow users to create and update user accounts to eventually link all purchases to their accounts.
<br>
<details>
<summary> User Stories for Epic: User Account Management</summary>
<br>

> [#14](https://github.com/leonp84/code-institute-project-5/issues/14) - As a **site user** I can **create a new account** so that I can **save my preferences, track orders, and make purchases**.

> [#15](https://github.com/leonp84/code-institute-project-5/issues/15) - As a **site user** I can **log in and log out** so that I can **access my account and securely sign out**.

> [#16](https://github.com/leonp84/code-institute-project-5/issues/16) - As a **site user** I can **confirm my email address** so that I can **verify my account and receive important notifications**.

> [#17](https://github.com/leonp84/code-institute-project-5/issues/17) - As a **site user** I can **log in using my Google account** so that I can **access the site quickly without creating a new account**.

> [#18](https://github.com/leonp84/code-institute-project-5/issues/18) - As a **site user** I can **update my user profile information** so that I can **keep my account details accurate and up-to-date**.

> [#19](https://github.com/leonp84/code-institute-project-5/issues/19) - As a **site user** I can **change my account password** so that I can **secure my account and update my login credentials**.

> [#20](https://github.com/leonp84/code-institute-project-5/issues/20) - As a **site user** I can **view a list of my past purchases** so that I can **track my order history and review previous transactions**.

> [#21](https://github.com/leonp84/code-institute-project-5/issues/21) - As a **site user** I can **view my wish list of favorite products** so that I can **save items for future consideration and purchase**.

</details>
<hr>

4. **[EPIC 4: Product Searching & Sorting](https://github.com/leonp84/code-institute-project-5/issues/28)** - A set of features that allow users to search and categorise products in the webstore.
<br>
<details>
<summary> User Stories for Epic: Product Searching & Sorting</summary>
<br>

> [#29](https://github.com/leonp84/code-institute-project-5/issues/29) - As a **site user** I can **search for products by name and description** so that **I can quickly find specific luxury watches**.

> [#30](https://github.com/leonp84/code-institute-project-5/issues/30) - As a **site user** I can **additionally search for products by category** (gender, brand, color, price) so that **I can narrow down my choices based on specific criteria**.

> [#31](https://github.com/leonp84/code-institute-project-5/issues/31) - As a **site user** I can **additionally sort listed products by category** (gender, brand, color, price) so that **I can organize search results according to my preferences**.

</details>
<hr>

5. **[EPIC 5: Purchase & Checkout](https://github.com/leonp84/code-institute-project-5/issues/32)** - A set of features that deals with the checkout process and payment functionality of the site.
<br>
<details>
<summary> User Stories for Epic: Purchase & Checkout</summary>
<br>

> [#33](https://github.com/leonp84/code-institute-project-5/issues/33) - As a **site user** I can **add a quantity of a product to my shopping bag** so that **I can purchase multiple items of the same product**.

> [#34](https://github.com/leonp84/code-institute-project-5/issues/34) - As a **site user** I can **add an item to my wishlist** so that **I can save it for future consideration or purchase**.

> [#35](https://github.com/leonp84/code-institute-project-5/issues/35) - As a **site user** I can **view my shopping bag details** so that **I can review the items I have selected for purchase**.

> [#36](https://github.com/leonp84/code-institute-project-5/issues/36) - As a **site user** I can **update my shopping bag by removing items** so that **I can adjust my selections before checkout**.

> [#37](https://github.com/leonp84/code-institute-project-5/issues/37) - As a **site user** I can **update the quantity of a product within my shopping bag** so that **I can adjust my purchase quantities before checkout**.

> [#38](https://github.com/leonp84/code-institute-project-5/issues/38) - As a **site user** I can **enter a custom delivery address** so that **I can receive my purchased items at a location of my choice**.

> [#39](https://github.com/leonp84/code-institute-project-5/issues/39) - As a **site user** I can **use a discount code during checkout** so that **I can apply promotional discounts to my purchase**.

> [#40](https://github.com/leonp84/code-institute-project-5/issues/40) - As a **site user** I can **add a watch care plan during checkout** so that **I can protect and maintain my purchased watch**.

> [#41](https://github.com/leonp84/code-institute-project-5/issues/41) - As a **site user** I can **save delivery details and create an account** upon checkout so that **I can save time on future purchases and manage my orders**.

> [#42](https://github.com/leonp84/code-institute-project-5/issues/42) - As a **site user** I can **pay securely via credit card** so that **I can complete my purchase with confidence**.

> [#43](https://github.com/leonp84/code-institute-project-5/issues/43) - As a **site user** I can **view order confirmation via email** so that **I have a record of my purchase and order details**.

</details>
<hr>

### Site Administrator

6. **[EPIC 6: Admin User Functionality](https://github.com/leonp84/code-institute-project-5/issues/23)** - A set of features that allow site superusers to add, edit or remove new products to the webstore.
<br>
<details>
<summary> User Stories for Epic: Admin User Functionality</summary>
<br>

> [#24](https://github.com/leonp84/code-institute-project-5/issues/24) - As a **site administrator** I can **add new products** so that **customers can browse and purchase new luxury watches**.

> [#25](https://github.com/leonp84/code-institute-project-5/issues/25) - As a **site administrator** I can **edit existing products** so that **I can update product information and keep it accurate**.

> [#26](https://github.com/leonp84/code-institute-project-5/issues/26) - As a **site administrator** I can **delete existing products** so that **I can remove outdated or discontinued items from the site**.

> [#27](https://github.com/leonp84/code-institute-project-5/issues/27) - As a **site administrator** I can **view statistics of past and current purchase details** so that **I can analyze sales performance and make informed business decisions**.

</details>
<hr>

<br>

[&uarr; Back to Top](#heritage-company)

# Business Model

Heritage Company sells **luxury timepieces** to upper middle-class clientele who either have sufficient disposable income (or are willing to take on debt) to outright purchase a product in the range of thousands of dollars. To understand this business model, it is it perhaps necessary to understand the philosophy behind luxury timepieces.

## Luxury Watches – The Philosophy

Luxury watches are, in the true sense, not rare items (since they are usually mass produced) but give the semblance of rarity and are undoubtedly icons of status among those that can afford them. Browsing the respective websites of the four popular Swiss watch brands sold on Heritage Company, it becomes clear that, while each target upper middle-class individuals with plenty of disposable income, each also variate somewhat is their precise demographic:

- [Tag Heuer](https://www.tagheuer.com/) / Sporty, adventure seeking up and coming professionals.
- [Breitling](https://www.breitling.com/) / Younger, upper middle-class buyers looking for a touch of tradition with their purchase.
- [Omega](https://www.omegawatches.com/) / An older, established clientele with more disposable income and higher-net worth than others on this list.
- [Tissot](https://www.tissotwatches.com/) / Lower end middle class buyers with less disposable income, but who want to take the first step into watch collection.

All four brands understand (and have inspired the business philosophy of Heritage Company) that with luxury timepieces, one sells not a mechanical product that customers use to check the time (though that too), but one primarily **sells a lifestyle and a story**. A story of rarity, luxury and status.

## Heritage Company – The Story

In the case of Heritage Company, the story is additionally built around the idea of family legacy and tradition. Of a luxury timepiece being an heirloom that travels with one through the important rites of passage, the milestones of life. This idea is reflected in the text on the landing page, the about us page, and of course, the company title!

To summarize: Heritage Company is designed with to reach a demographic of younger, up and coming middle and upper-middle class clientele, who are possibly starting families, and have disposable income or the ability to quickly procure debt.

<br>

[&uarr; Back to Top](#heritage-company)

# Marketing Strategy

The three primary goals, the driving force behind the site design and UX of heritage-company.net are (in order of importance):

(1) **Make a purchase**: Buy a single item (or multiple items), making use of the upselling during checkout for additional profit.<br>
(2) **Sign up for a newsletter**: Studies consistently show that potential customers interact better with niche-driven email marketing, than general marketing such as Google AdWords.<br>
(3) **Create an account**<br>

To this end, the site funnels users, from the landing page, towards specific products and the eventual checkout process. Making the shopping and checkout process as _frictionless as possible_. Newsletter sign-ups are encouraged, by making use of static and additional dynamic sign-up notifications. And creating an account is a simple process needing just an email address and password.

## Future Marketing Ideas

Future marketing strategies should incorporate **blog articles** about watch collection and luxury timepiece related news. For (especially) collectors, fresh watch-related information, presented in a well written (and SEO spider friendly) manner are highly desirable. Investing in good written material, produced by a luxury watch expert, could be a valuable selling strategy to keep users coming back. These articles can then of course be promoted through the site newsletter or social media pages.

To that end, the site also employs social media marketing through a dedicated [Facebook Business page](https://www.facebook.com/profile.php?id=61562008868047). Screenshots of the Facebook page are also available below.

<details>
<summary> Facebook Business Page Screenshots</summary>

![Heritage Company Facebook Business Page Screenshot](static/assets/images/readme-images/facebook1.jpg)
<br>

![Heritage Company Facebook Business Page Screenshot](static/assets/images/readme-images/facebook2.jpg)
<br>

![Heritage Company Facebook Business Page Screenshot](static/assets/images/readme-images/facebook3.jpg)
<br>

![Heritage Company Facebook Business Page Screenshot](static/assets/images/readme-images/facebook4.jpg)
<br>

</details>
<hr>

<br>

<br>

[&uarr; Back to Top](#heritage-company)

# SEO

During the planning stage of the project, [Wordtracker](https://www.wordtracker.com/) was used to identify some of the most useful and valuable SEO words related to luxury watches, Swiss watches and the four brands of watches that are sold on heritage-company.net. These keywords were then incorporated in different parts of the site design, especially page titles, `<h1>` tags, image alt descriptions, meta descriptive tags, and as general keywords throughout the text content of the site (naturally avoiding any semblance of keyword stuffing).

_Keyword Results courtesy of the free version of Wordtracker_

![Wordtracker Keyword Results](static/assets/images/readme-images/wordtracker.jpg)

## Google Search Console

After registering the domain with Google search console and verifying ownership by updating the DNS records, the [sitemap.xml](https://heritage-company.net/sitemap.xml) and [robots.txt](https://heritage-company.net/robots.txt) files were submitted to Google search console.

_Sitemap.xml report from Google Search Console_

![Heritage Company](static/assets/images/readme-images/sitemap.jpg)

The site was successfully crawled, with robots.txt showing no errors, and shows up in Google search results when searching, for example using the phrase “heritage company watches”. Note that Google search results are (to a degree) location and user specific so the same results might not show up for others.

_Robots.txt report from Google Search Console_

![Heritage Company Robots.txt with Google Search Console](static/assets/images/readme-images/robots.jpg)

<br>

[&uarr; Back to Top](#heritage-company)

# Site Design

## Visuals

The site design speaks to the targeted customer demographic by incorporating sleek visuals and dark and black themes (associated with luxury). The following colour palette was used throughout.

_Colour Palette by [Coolors.co](https://coolors.co)_

![Site Colour Palette](static/assets/images/readme-images/colour-palette.jpg)

## Logo

The website logo was created with the help of the AI Logo creation tool from [Looka](https://www.looka.com). It features the company name and a fire symbol in gold, surrounded by a golden border. The fire symbol was chosen as the company identifier since it ties in with the Heritage/Legacy theme espoused on the landing page and about us page. It is based on the quote from Gustav Mahler: _‘Tradition is not the worship of ashes, but the transmission of fire.'_

<img src="static/assets/images/readme-images/logo.jpg" alt="Heritage Company Logo" width=350>
<br>

## Wireframing

During the planning phase of the project, wireframes was designed for desktop and mobile versions of the main landing page, the product list display page, and a product details page. The current, deployed version of the project closely resembles these original designs.

Wireframing was done with [Balsamiq](https://balsamiq.com/) software.

_Landing Page Wireframe_

![Landing Page Wireframe](static/assets/images/readme-images/wireframe-landing.jpg)

_Product Display Page Wireframe_

![Product Display Page Wireframe](static/assets/images/readme-images/wireframe-products.jpg)

_Product Details Wireframe_

![Product Details Wireframe](static/assets/images/readme-images/wireframe-detail.jpg)

## Flowchart

During the planning phase, the following flowchart was designed to show customer/user interaction with the website. The flowchart includes database interaction, but some elements (such as the ‘Review Shopping Experience’ step post order) was abandoned during development as it didn’t fit the vision of the project. The flowchart was designed with [Lucidchart](https://www.lucidchart.com/pages/).

![Website Flowchart](static/assets/images/readme-images/flowchart.jpg)

From an e-commerce perspective, the red lines show the preferred, and most desirable, navigation path a user can take.

## Model Design and Relationships

The Entity Relationship Diagram (ERD) below (by [dbdiagram.io](https://dbdiagram.io/)) visually displays the database design. For more detailed explanations of the relationships between models, and their purpose, it is recommended to read the Django view docstrings in the respective views.py and models.py pages of each app. There the model relationships are explained in detail.

![Heritage Company Database Design](static/assets/images/readme-images/erd.jpg)

<br>

[&uarr; Back to Top](#heritage-company)

# Features

## Landing Page

The site landing page was designed to be as visually arresting and enticing for first time visitors as possible, while not being too distracting or cluttered. At the top of the landing page, the hero section consists of a carousel of two particularly sought after luxury timepieces that customers can view and buy. Using visually arresting imagery here sets the tone for the rest of the landing page.

_Hero Section Image Carousel_

![Hero Carousel Image](static/assets/images/readme-images/hero-carousel.jpg)

The four brands of Swiss watches sold on heritage-company.net are then shown as clickable visual links (with a hover effect) encouraging users to start browsing products.

_Links to Product Brands_

![Product Brands](static/assets/images/readme-images/product-brands.jpg)

The rest of the landing page consists of text and imagery, including a parallax image and some customer testimonials, setting the stage for customers to browse further. Three popular products are also shown on the landing page.

![Landing Page Imagery](static/assets/images/readme-images/landing-page-extra.jpg)

The landing page uses visual effects where certain parts of the page dynamically blends into view as the user scrolls down the page.

## Header

The site header, displayed on every page, contains the company logo, name, and slogan, and account related links for users to search products, see their profiles, see their shopping bags, and contact the business. Below the header, an additional sticky navigation bar that lists links to the main product pages is shown. This remains visible to the user when they scroll down the page and ensures the most important links (for customers to make purchases) are consistently visible to users.

_The site header in desktop mode_

![Header Desktop](static/assets/images/readme-images/header.jpg)

The site header dynamically updates depending on the screen width size, it is fully responsive showing the maximum number of information and icons in desktop mode, and only a minimum number of icons, with a drop-down menu, in mobile mode.

_The site header on small (mobile or small tablet) screens_

![Header Mobile](static/assets/images/readme-images/header-mobile.jpg)

## Footer

Along with the header, the site footer is displayed on every page and contains two rows. The first row contains 3 columns: The 1st with a newsletter sign-up option where customers are encouraged to submit their e-mail addresses and receive the heritage company newsletter. The second column with links to various parts of the site. And the third column containing two (no-follow) social links to Facebook and LinkedIn, that open in new browser tabs. The footer is also fully responsive, showing fewer items in mobile mode. The newsletter signup remains present throughout.

![Footer](static/assets/images/readme-images/footer.jpg)

The final row in the footer contains the copyright information and links to the privacy policy, terms and conditions, and the GitHub repository of the site designer.

## Newsletter Sign-up

On top of the static newsletter sign up form that are always displayed to users in the footer, an additional dynamic sign-up form is displayed to each user once per 24 hours.

**NOTE:** _This 24-hour timer (a Django session variable) can be reset by visiting the site’s privacy policy page. That view resets the session variable and I specifically left it there to make testing this additional sign-up modal easy._

<img src="static/assets/images/readme-images/newsletter-extra.jpg" alt="Newsletter Sign-up Modal" width=450>
<br>

This additional newsletter sign-up modal slides in to view from the left border of the site once the user has scrolled down to at least 75% of the page contents of whatever page they are currently browsing. Users can then either submit the form or close this modal by clicking on the X. The gentle sliding animation, and the fact that users are not bombarded with this message at every visit of the site, means that it is only slightly obtrusive, but as statistics show can lead to a high increase in newsletter sign-ups.

Upon submitting the newsletter sign up form, users are redirected to a page asking them to confirm their e-mail addresses. When users visit their inbox and click on the e-mail confirmation link, they are brought back to heritage-company.net, where they are presented with a message that their newsletter sign up has been successful.

<img src="static/assets/images/readme-images/email-verify.jpg" alt="Verification Email to Customer" width=450>
<br>

As enticement for users to sign up to the newsletter, a **discount code** is given to them upon successful e-mail verification. This discount code is dynamically generated and consists of 6 digits, both letters and numbers. Upon successful e-mail verification the code is generated, saved in the database, and then emailed to the customer in an additional, separate email. This code is then available for use during the checkout process.

<img src="static/assets/images/readme-images/discount-code.jpg" alt="Discount Code" width=450>
<br>

## All Products

The All products page allows users to see the entire catalogue of watches available for purchase on heritage-company.net. All pages that display products in this manner use a grid system whereby each watch is contained within a box, showing a watch image and basic information including the product price below the image.

![All Products Page](static/assets/images/readme-images/all-products.jpg)

Watch images have a hover effect where if the user **hovers** with the mouse over the product display box, a _special effect_ switches the image of the watch to a different one and employs a zoom effect with transition. This provides a pleasant browsing experience for the user as they scroll through the selection of watches.

![Hover Effect](static/assets/images/readme-images/hover-effect.gif)

Each page that displays products also have a sticky search and filter bar that stays fixed the top of the page as the user scrolls down. This bar contains 2 buttons: A ‘Sort’ button that allows the user to reload the current page with the products sorted by price, either descending or ascending.

![Filter and Search Bar](static/assets/images/readme-images/filter-and-search.jpg)

And a ‘Search’ button which, when clicked, scrolls back to the top of the page and opens the search bar allowing users to do basic keyword search of products. Clicking on any of the displayed products on this page will then take the user to a dedicated product detail page. More on that below.

## Brand Specific Pages

The site was deployed with 33 products in the catalogue/database (Superusers can of course add additional products. All luxury timepieces on heritage-company.net fall under one of four famous Swiss watch brands: Breitling, Tag Heuer, Omega, and Tissot. Clicking on the navigation bar link for one of these four companies then takes the user to a page displaying time pieces of that specific brand.

_The Breitling Product Page_

![Brand Specific Pages](static/assets/images/readme-images/brand-specific.jpg)

Like the ‘All Products’ page, listed products have a hover transition effect and clicking on any of the watch images leads users to a dedicated product page.

## Discounted Products

A final category of watches are discounted items that users can reach by clicking on the sale button in the navigation bar. This displays watches of all brands that are currently on discount.

![Discounted Products](static/assets/images/readme-images/sale.jpg)

Discounted items are displayed similarly as on other pages but have an addition of a discount percentage icon displayed in the top right of the product box. An updated price with discount considered, is also shown to the user.

## Product Search

On both the desktop and mobile versions of the navigation bar in the header, a search icon appears. Clicking on the search icon dynamically reveals a search bar that allows users to do basic keyword search.

![Search Bar](static/assets/images/readme-images/search-bar.jpg)

Any keywords entered into the search bar and then submitted, returns a list of search results where the keywords are either in the title or description of the watches. The search bar also contains a filter icon that allows users to do advanced search using product filter.

![Search Results](static/assets/images/readme-images/search-results.jpg)

## Advanced Search

The advanced search function allows users to search products by keyword using additional filters: watch brand, gender, dial colour and price range. Users can select some or all of the filters, and include keywords, or no keywords, as part of the search query.

<img src="static/assets/images/readme-images/advanced-search.jpg" alt="Advanced Search" width=550>
<br>

Results then take into account all of the submitted information to return a query set of products matching the user’s filters. If no keywords were entered, this is indicated to the user on the search result page, but an additional message makes sure the user is aware that their other filters were taken into account during the search process.

<img src="static/assets/images/readme-images/advanced-search-results.jpg" alt="Advanced Search Results" width=550>
<br>

## Product Details Page

The product detail page is where users can see all relevant information of a timepiece: its brand, title, price, description, watch case size, watch dial colour, and gender. Each product page displays a main image for the specific timepiece and two additional images that users can Click to see a full version of. Each currently focused image again has the option to be clicked revealing a near full screen size model with a large, zoomed version of the image.

![Product Detail Images](static/assets/images/readme-images/product-detail-images.gif)

Other features of this page include the ability to contact the store owner regarding a specific product, to add the watch to the user's shopping bag, and to add the item to the user's wish list.

Hovering over the bookmark icon displays a Bootstrap tooltip explaining to users that it's possible to add this image as a bookmarked image to their wish list.

<img src="static/assets/images/readme-images/bookmark.jpg" alt="Bookmark a Product" width=550>
<br>

Upon clicking this icon an asynchronous JavaScript message is sent to the server to determine whether the user is currently logged in an authenticated. If the user is logged in parenthesis and therefore has an active wish list), the item is added to the authenticated users wish list. If not, a special modal shows up encouraging users to sign in or create an account to add items to the wish list.

<img src="static/assets/images/readme-images/create-account-to-bookmark.jpg" alt="Create Account Modal" width=550>
<br>

From a business perspective the most important button on this page is of course the ‘Buy this Watch’ button. When users click this a loading animation shows up and after 2 seconds a success message indicated that the watch was added to the user's shopping bag. At the same time the number of items in the bag is automatically updated in the NAV bar giving clear visual feedback to the user.

![Customer clicks the buy button](static/assets/images/readme-images/click-buy-button.gif)

Users are limited to a Max of three items per product per shopping bag, and once users have reached this limit and try to add additional quantities of the same product to their bags, error message displays that the product limit has been reached.

<img src="static/assets/images/readme-images/limit.jpg" alt="Limit Reached Message" width=550>
<br>

<br>

[&uarr; Back to Top](#heritage-company)

## Product Contact

Clicking on the ‘Enquire’ button on any product details page opens a contact us modal. This modal contains 4 fields, two of which (the product related fields) are automatically pre-populated. If a user is authenticated and his or her name and e-mail address is saved to the database, this information is also pre-filled in the contact us form. In such a case the user only needs to type their message and click on the send message button. Submitting this form creates a message instance that is saved to the database and can be viewed by a superuser from the accounts page.

![Product Contact Form](static/assets/images/readme-images/product-contact.jpg)

Successful form submission displayed a success message to users so that they know their message has been sent.

## Accounts: Sign-up and Login

Clicking on the accounts icon in the navigation bar leads users to a sign in Page if they are not yet authenticated. Here it is possible to sign in with an e-mail address and password. It is also possible to sign in with Google, using Django AllAuth social login library.

![Account Login](static/assets/images/readme-images/sign-in.jpg)

Users can also sign up for an account at heritage-company.net using an e-mail address and strong password, or similarly sign up using the Google social signup service. Users that have forgotten their passwords can also click the relevant link to be sent a password reset e-mail.

When creating new accounts, users are asked to verify their email address. They are automatically sent an email with a verification link. Clicking this link activated their accounts and redirects them to the login page.

Login, Logout and other similar account related action include success or failure messaging to the user (displayed via bootstrap toasts in the bottom left corner of the site), to ensure constant visual feedback is provided to users.

## Accounts: Profile Page

After account creation and login, the accounts icon takes users to their profile pages. Here they are personal and delivery information is displayed. Their wish list is shown, and a list of past purchases are also available. If no profile information is currently available for the new user, they are encouraged to update their profile and save the information so that this can automatically be used during checkout.

![My Account Page](static/assets/images/readme-images/my-account.jpg)

## Wish List

When users are logged in and choose to add specific products to their wish list, these items then show up in the wish list of the user on their accounts page. Users can easily remove items from their wish list by simply clicking the X or delete button next to any item in the wish list. All actions like these include messaging to show the user that their wish list has been successfully updated. This is also done through asynchronous JavaScript to avoid unnecessary page refreshes.

<img src="static/assets/images/readme-images/wish-list.jpg" alt="Customer Wish List" width=550>
<br>

## Past Orders

The past purchases section of the ‘My account’ page lists each past purchase the customer has made on heritage-company.net. This includes vital order information such as the date, total and delivery information. Products and quantities ordered, as well as the prices and a watch care plan selection, is also shown in this section.

![Customer Past Orders](static/assets/images/readme-images/past-purchases.jpg)

## Shopping Bag

The shopping bag page lists all items currently in the user shopping bag: Showing watch information, price, a quantity selector and a delete button for each item in the shopping bag. Users can update the quantities up to a maximum of three and the subtotal of the order is automatically calculated without page refresh, thanks to asynchronous JavaScript. Users can delete each product in the shopping bag also causing the subtotal to dynamically update.

![Shopping Bag Interactions](static/assets/images/readme-images/shopping-bag-interactions.gif)

In the column displaying the current order subtotal the user is also given the option to add a watch care plan with some information text explaining that for a fee of 2.5% of the order total each purchased timepiece comes with service and cleaning benefits.

Clicking this button also dynamically upsets the subtotal by adding 2.5% to the final price. The final price is constantly updated (with a visual loading spinner) when users make changes to the any interactive element on the page (item quantity, deleting items, adding watch care plan). This ensures the order total remains up to date and users are clearly informed through constant visual feedback.

![Full Shopping Bag](static/assets/images/readme-images/shopping-bag-final.jpg)

A yellow ‘Proceed to Checkout’ button redirects users to the checkout page. If all items have been removed from the shopping bag, this button is greyed out and disabled.

Finally, if users visit their shopping bag, but the bag is empty, a separate message encourages users to browse the product catalogue first.

## Checkout

On checkout users are redirected to a visually distinct checkout page without the regular header and footer of the rest of the site. This is to ensure a focused and distraction free checkout environment and is similar to the practice followed by many e-commerce stores. Here the order details and total are presented in table form and users are asked to fill in their personal and delivery information including any special instructions needed to fulfil the order. Logged in users (that have completed their profile data) naturally have this checkout form pre-populated with their data. Users are encouraged to sign in (before filling in the form) if they want to make use of this feature.

![Checkout Page](static/assets/images/readme-images/checkout-page.jpg)

Below the ‘Continue to Payment’ button users here also have the option to enter a discount code. Upon Newsletter sign up, as mentioned above, users are given a six digit randomly generated discount code that automatically provides a $100 discount to any order on heritage-company.net. Entering the code here and clicking on the check code validity button, sends the code to the Django back end, via asynchronous JavaScript, where the code is checked against the database.

![Redeem Discount Code](static/assets/images/readme-images/discount-code.gif)

If the code is valid (i.e. currently in the database), a success message is shown to users and $100 taken off the grand total price of the order. If not, an error message is displayed, and users are given the opportunity to try again. The final step in locking in any discount is to then click on the continue to payment button.

## Create Account upon checkout

Before proceeding to payment, users are given the opportunity to create an account with a temporary password, saving their current delivery details to their new accounts. This option is of course only available to non-authenticated users.

<img src="static/assets/images/readme-images/create-account-checkout.jpg" alt="Create Account upon Checkout" width=550>
<br>

If this option is chosen and the ‘Continued to Payment’ button is clicked, then a new user account with a randomly generated 8-digit strong password is created (using the order e-mail address as login), and the user is sent an account verification e-mail, and a separate e-mail with their temporary password. If non-authenticated users try to create an account using an email that is already tied to an existing account, users are shown an error message and returned to the landing page. From here they can login and complete the order.

These are sent using Gmail's SSL encrypted SMTP server. Users are then encouraged to verify their e-mail address, log in with their temporary password, and naturally change their password as soon as possible.

<img src="static/assets/images/readme-images/account-created-email.jpg" alt="Temporary Password Emailed" width=550>
<br>

This is the only part of the order that is completed before order confirmation (i.e. before order payment), since creating a new user account is not dependent on having completed an order, and its better for the store to have more user accounts (and email contact of potential clients), even is these do not make an initial purchase.

## Order Payment

The order payment page provides a very visually minimalistic design, where the grand total in U.S. dollars (including any discounts from the previous page) is displayed along with a credit card check out box. Heritage-company.net uses Stripe’s integrated credit card payment functionality. The stripe payment box provides users with its own visual feedback during payment processing, or in case any errors (such as invalid card details provided) pop up.

![Order Payment](static/assets/images/readme-images/order-payment.jpg)

## Order Confirmation

After Stripe has verified successful credit card payment users are redirected to the order confirmation page, where order details are shown to them, and they are thanked for their business. Users are also informed to check their e-mail inboxes since an e-mail containing similar information is sent to them.

## Superuser Functionality

Throughout the site, users that are authenticated with superuser credentials, are given privileges to manage the heritage-company.net storefront. On, for example, every product detail page, a separate box with options is shown to super users (called store administrators) where users are able to edit or delete the product shown on the current page.

<img src="static/assets/images/readme-images/superuser-product-details.jpg" alt="Superuser Product Details" width=700>
<br>

The same options are also available for superusers on their accounts pages where they are given a dropdown menu of all current products on the store front (sorted alphabetically by brand name) in order to add or delete existing products.

![Superuser Account](static/assets/images/readme-images/superuser-account.jpg)

Upon choosing to delete an existing product, superusers are taken to a separate page where the current product is displayed, a warning message given, and explicit confirmation required before a product is deleted from the storefront.

![Delete Product](static/assets/images/readme-images/delete-product.jpg)

Upon choosing to edit an existing product, superusers are taken to the edit product page where a pre-populated form of the current product, including image fields, is presented. Form validation is included in this submission process and any changes are immediate. After editing a product, users are redirected to the updated product's details page to see their changes along with a confirmation message.

<img src="static/assets/images/readme-images/edit-product.jpg" alt="Edit Product" width=600>
<br>

If from their accounts page a super user chooses to add a new product this is a rather simple process. The ‘Add product’ page presents the same (now empty) product form asking users to provide the details of the new product including at least one image. This form provides helpful text notes under most product fields for super users so that they can complete the details of the new product in a way that matches the style of other products on the storefront. If the new product form is submitted and passes validation users are redirected to the new product page and a success message displayed as confirmation.

<img src="static/assets/images/readme-images/add-new-product.jpg" alt="Add New Product" width=600>
<br>

## Superuser Statistics

On the accounts page of superusers, they are also given links to statistics of the current messages, orders, and subscribers to the site. Each of these links does take the user to the customised back-end admin panel (designed by Django but customised for the heritage company storefront).

Superusers can view recent orders, including all order details and products ordered. Superuser can also see any recent messages and a list of current newsletter subscribers. All these statistics are presented in custom Django admin models to make them as user friendly as possible.

_Admin Extra Functionality_

![Admin Extra](static/assets/images/readme-images/admin-extra.jpg)

_Superusers can view recent orders, and other information on the admin page_

![Recent Orders](static/assets/images/readme-images/recent-orders.jpg)

## Miscellaneous Pages

The site includes an about us page with some motivational text for potential customers, including a fictional back story for on origin of heritage company. A contact us page is also available with a customer contact form. The page also includes a frequently asked questions section that users are asked to read before submitting the contact form.

Privacy policy, and Terms and Conditions pages are also available via links found in the site footer The content of these pages were generated using online tools, and the privacy policy includes the necessary additional information to comply with the European General Data Protection Regulation (since the site is based in Austria).

_The About Us Page_

![About Us](static/assets/images/readme-images/about-us.jpg)

<br>

[&uarr; Back to Top](#heritage-company)

# Testing

## Manual Testing

<br>
<details>
<summary>General Navigation</summary>
<br>

| Expected Outcome                                       | Test Procedure                                                                 | Result |
| ------------------------------------------------------ | ------------------------------------------------------------------------------ | ------ |
| All links on the site footer open to the correct pages | Click on each link in the footer to ensure they open to the correct pages      | Pass   |
| All links on the header open to the correct pages      | Click on each link in the header to ensure they open to the correct pages      | Pass   |
| All links on the desktop navigation bar work correctly | Click on each link in the desktop navigation bar to ensure they work correctly | Pass   |
| All links on the mobile navigation bar work correctly  | Click on each link in the mobile navigation bar to ensure they work correctly  | Pass   |
| The site's custom 404 page works correctly             | Navigate to a non-existent page to verify the custom 404 page appears          | Pass   |

</details>

<br>
<details>
<summary>Product Viewing & Browsing</summary>
<br>

| Expected Outcome                                              | Test Procedure                                                                            | Result |
| ------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ------ |
| User can browse all products                                  | Click through each product category and subcategory to ensure all products are accessible | Pass   |
| User can browse products by brand                             | Click on each brand category to ensure products are accessible                            | Pass   |
| User can browse products that are on sale                     | Navigate to the sale section to ensure all sale products are accessible                   | Pass   |
| Users can click on any product for more detail                | Click on each product to verify detailed information is displayed                         | Pass   |
| Users can contact site management regarding specific products | Use the contact form for specific products to ensure it functions correctly               | Pass   |

</details>

<br>
<details>
<summary>Search & Results</summary>
<br>

| Expected Outcome                                    | Test Procedure                                                                    | Result |
| --------------------------------------------------- | --------------------------------------------------------------------------------- | ------ |
| User can accurately search products by keywords     | Enter various keywords in the search bar to ensure accurate results are displayed | Pass   |
| User can accurately search products by brand        | Search for different brands to ensure accurate results are displayed              | Pass   |
| User can accurately search products by watch gender | Search by gender categories to ensure accurate results are displayed              | Pass   |
| User can accurately search products by dial colour  | Search by dial colour to ensure accurate results are displayed                    | Pass   |
| User can accurately search products by price range  | Use the price range filter to ensure accurate results are displayed               | Pass   |

</details>

<br>
<details>
<summary>Accounts & Login</summary>
<br>

| Expected Outcome                                                  | Test Procedure                                                                          | Result |
| ----------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------ |
| Users can create an account with email signup                     | Complete the email signup process to ensure account creation works                      | Pass   |
| Users can create an account with Google signup                    | Complete the Google signup process to ensure account creation works                     | Pass   |
| Users can verify their email addresses after signup               | Verify the email address to ensure the verification process works                       | Pass   |
| Users can change their passwords                                  | Change the password to ensure the process works correctly                               | Pass   |
| Users can view their wish list in their accounts page             | Navigate to the wish list in the account page to ensure it displays correctly           | Pass   |
| Users can view their past orders in their accounts page           | Navigate to the past orders section in the account page to ensure it displays correctly | Pass   |
| Users can update their profile information in their accounts page | Update the profile information to ensure changes are saved correctly                    | Pass   |

</details>

<br>
<details>
<summary>Superuser Functionality</summary>
<br>

| Expected Outcome                              | Test Procedure                                                                            | Result |
| --------------------------------------------- | ----------------------------------------------------------------------------------------- | ------ |
| Superusers can add products to the storefront | Log in as a superuser and add new products to ensure the process works correctly          | Pass   |
| Superusers can edit existing products         | Log in as a superuser and edit existing products to ensure changes are saved correctly    | Pass   |
| Superusers can delete existing products       | Log in as a superuser and delete products to ensure the process works correctly           | Pass   |
| Superusers can view site statistics and usage | Log in as a superuser and navigate to the statistics page to ensure it displays correctly | Pass   |

</details>

<br>
<details>
<summary>Newsletter</summary>
<br>

| Expected Outcome                                                | Test Procedure                                                                | Result |
| --------------------------------------------------------------- | ----------------------------------------------------------------------------- | ------ |
| Users can sign up for a newsletter via the footer               | Use the newsletter signup form in the footer to ensure it functions correctly | Pass   |
| Users can sign up for a newsletter via the slide in signup form | Use the slide-in signup form to ensure it functions correctly                 | Pass   |
| Users receive email confirmation upon sign up                   | Sign up for the newsletter and verify receipt of confirmation email           | Pass   |
| Users receive a discount code upon email verification           | Complete email verification and ensure a discount code is received            | Pass   |

</details>

<br>
<details>
<summary>Customer Messaging</summary>
<br>

| Expected Outcome                                                        | Test Procedure                                                         | Result |
| ----------------------------------------------------------------------- | ---------------------------------------------------------------------- | ------ |
| Users are notified when successfully logged in                          | Log in to the site to ensure a notification is received                | Pass   |
| Users are notified when successfully logged out                         | Log out of the site to ensure a notification is received               | Pass   |
| Users are notified when a contact form is submitted                     | Submit a contact form to ensure a notification is received             | Pass   |
| Users are notified when a product is added to the cart                  | Add a product to the cart to ensure a notification is received         | Pass   |
| Users are notified when their shopping bag has been updated             | Update the shopping bag to ensure a notification is received           | Pass   |
| Users are notified when they have bookmarked an item                    | Bookmark an item to ensure a notification is received                  | Pass   |
| Users are notified when they have removed an item from their wish lists | Remove an item from the wish list to ensure a notification is received | Pass   |
| Users are notified when an order has been successfully paid             | Complete a payment to ensure a notification is received                | Pass   |

</details>

<br>
<details>
<summary>Purchasing Process</summary>
<br>

| Expected Outcome                                                                 | Test Procedure                                                                    | Result |
| -------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | ------ |
| Users can add items to their shopping bag                                        | Add items to the shopping bag to ensure the process works correctly               | Pass   |
| Users can add up to 3 of the same items to their shopping bag                    | Add three of the same item to the shopping bag to ensure the limit is enforced    | Pass   |
| Users can update product quantity in their shopping bags                         | Update the product quantity in the shopping bag to ensure changes are saved       | Pass   |
| Users can remove items from their shopping bags                                  | Remove items from the shopping bag to ensure the process works correctly          | Pass   |
| Users can add a watch plan during checkout                                       | Add a watch plan during checkout to ensure the option is available                | Pass   |
| Users can log in during the checkout process to speed up the process             | Log in during checkout to ensure the process is expedited                         | Pass   |
| Users can choose to create an account upon checkout                              | Opt to create an account during checkout to ensure the process works              | Pass   |
| Users can enter a new delivery address (or use an existing one), during checkout | Enter a new delivery address during checkout to ensure it can be saved and used   | Pass   |
| Users can use a discount code for $100 discount during the checkout process      | Apply a discount code during checkout to ensure the discount is applied correctly | Pass   |

</details>

<br>
<details>
<summary>Payment Process</summary>
<br>

| Expected Outcome                                                       | Test Procedure                                                                            | Result |
| ---------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ------ |
| Users can pay via credit card                                          | Complete a payment via credit card to ensure the process works correctly                  | Pass   |
| Users are notified if their credit card presents errors                | Attempt a payment with an invalid credit card to ensure an error notification is received | Pass   |
| Users are notified if their orders are successful                      | Complete an order to ensure a success notification is received                            | Pass   |
| Users receive an email notification upon successful payment completion | Complete a payment and verify receipt of the email notification                           | Pass   |

</details>

<br>
<details>
<summary>Miscellaneous Pages and Functions</summary>
<br>

| Expected Outcome                             | Test Procedure                                                            | Result |
| -------------------------------------------- | ------------------------------------------------------------------------- | ------ |
| Users can view the about us page             | Navigate to the about us page to ensure it displays correctly             | Pass   |
| Users can view the site privacy policy       | Navigate to the privacy policy page to ensure it displays correctly       | Pass   |
| Users can view the site terms and conditions | Navigate to the terms and conditions page to ensure it displays correctly | Pass   |
| Users can contact site management            | Use the contact form to ensure it functions correctly                     | Pass   |

</details>

<br>
<details>
<summary>Testing For Responsiveness</summary>
<br>

| Test                                                      | Result |
| --------------------------------------------------------- | ------ |
| Site displays correctly on screens between 320px & 479px  | Pass   |
| Site displays correctly on screens between 480px & 767px  | Pass   |
| Site displays correctly on screens between 768px & 1199px | Pass   |
| Site displays correctly on screens 1200px and larger      | Pass   |

</details>

<br>
<details>
<summary>Cross Browser Testing</summary>
<br>

| Browser | Resolution | Result    | Issues |
| ------- | ---------- | --------- | ------ |
| Chrome  | 1440px     | Very Good | None   |
| Edge    | 1440px     | Very Good | None   |
| Firefox | 1440px     | Very Good | None   |
| Safari  | 768px      | Very Good | None   |

</details>

## Automated Testing

A total of **30 automated tests** were written to continually check the site integrity before deployment. As of final deployment all tests are passing.

<details>
<summary> Automated Testing </summary>
<br>

The Python [Coverage](https://coverage.readthedocs.io/en/7.5.1/) library is showing a total automated test covering of 76% for the app. That takes into account all files for the entire application, though the view.py files by themselves have lower coverage.

The following test files contain automated tests for various models, forms and views.

> product/test_views.py
> product/test_models.py
> product/test_forms.py

> main/test_views.py
> main/test_models.py
> main/test_forms.py

> my_account/test_models.py
> my_account/test_forms.py

> my_account/test_models.py
> my_account/test_forms.py

![Automated Tests Coverage for Heritage Company](static/assets/images/readme-images/coverage.jpg)

</details>
<br>

## Validator Testing

**HTML** | Upon final deployment no errors were returned when passing through the official W3C validator. The results for a few key pages are below. Other pages can be checked manually.

- [index.html Validator Results](https://validator.w3.org/nu/?doc=https%3A%2F%2Fheritage-company.net%2F)
- [all_products.html Validator Results](https://validator.w3.org/nu/?doc=https%3A%2F%2Fheritage-company.net%2Fproduct%2Fall_products%2F)
- [product_detail.html Validator Results](https://validator.w3.org/nu/?doc=https%3A%2F%2Fheritage-company.net%2Fproduct%2Fproduct_detail%2F24)
- [about_us.html Validator Results](https://validator.w3.org/nu/?doc=https%3A%2F%2Fheritage-company.net%2Fabout%2F)

**CSS** | Upon final deployment, no errors were returned when passing through the official W3C (Jigsaw) validator.

- [style.css Jigsaw Validator Results](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fheritage-company-s3.s3.eu-central-1.amazonaws.com%2Fstatic%2Fassets%2Fcss%2Fstyle.css&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)

**JavaScript** | Upon final deployment, almost no errors were returned when passing the JavaScript through the JSHint validation tool. On some pages warnings (not errors) were given regarding functions undeclared functions. Since this dealt mostly with the Django CSFR token declared elsewhere in the HTML page, I deemed it acceptable.

**Python** | Upon final deployment, no errors were found when passing the edited Django Python files through the [CI Python Linter](https://pep8ci.herokuapp.com/)

**Lighthouse** | The site was tested with Google Lighthouse using Chrome Developer Tools. I find the lighthouse testing somewhat erratic and the results are never exactly the same (specifically the 'performance' metric). It jumps between a result in the high 80's to low 90's. One such result for index.html is shown below.

![Lighthouse Test Results](static/assets/images/readme-images/lighthouse.jpg)

[&uarr; Back to Top](#heritage-company)

# Bugs

<details>
<summary> Bugs Details </summary>
<br>

- The official W3 **HTML Validator showed a multitude of errors**, primarily on the index.html and my_account.html files. These consisted of multiple ‘id’ errors or incorrect aria labelling. On the ‘My_Account’ page, the template renders a model function (:model:`checkout.Order.items_ordered`) that returns a HTML table element. With the external HTML being injected into the page, the validator showed additional errors that needed correcting. This was done by tweaking the HTML output of the model function.

- By using the VSCode _ESLint_ and _Prettier_ extensions during production, most of the common JavaScript linting errors that pops up during coding was avoided, but the linter still showed many **undeclared variables** that needed updating.

- Incorporating the **Stripe JavaScript code** during the checkout process proved challenging, produces many bugs and rounds of testing. I found the Stripe recommended [JavaScript integration](https://docs.stripe.com/payments/quickstart?lang=python) quite opinionated, and it didn’t fit well with my site architecture. Site’s insistence on providing a redirect URL after successful payment meant I needed to update my `checkout.views` to accommodate this and create the new order instance only after Stripe’s redirect (when payment is confirmed).

- Using both Stripe for checkout, and AWS for static and media file storage, means I consistently needed to tweak the project settings.py file in order for all functionality to work in **both production and deployment environments**. One example would the be settings.SITE_URL variable that needs to be updated in the production environment.

- Getting the visual display and **responsiveness of the mobile navbar** just right, proved somewhat complicated. Since the navbar dynamically updated (without page refresh) when the shopping bag is updated, it took some CSS positioning tweaking to get all elements (especially the shopping bag icon) to display correctly in all screen sizes.

- In general, with a larger project like this, consistently designing pages to be fully responsive from 320px pixels upward produced some bugs. I often had to go back to previously designed pages to update new header or footer elements (or new content in the page) to **maintain responsive design**.

- The idea to produce an image change and zoom effect when a user hovers over a product (on a product list display page), proved buggy, primarily because the **images tended to load to slow**, negative the impact of the effect. This was corrected by preloading the images upon page load, using the JavaScript `new Image()` functionality.

- Loading product images via fixtures proved uncomplicated, by the images from Tissot (having come for a different source than those of the other brands) had a completely white background, leading to **visual discontinuity** when a user’s shopping bag (or wish list) contained both a Tissot product, and one from another brand. To solve this, I manually edited the Tissot product main images with an image editor to give the background a similar colour to those of other brands.

- When **manually creating a new customer** (if desired by the customer, upon checkout) Django didn’t allow me to manually set passwords for new accounts. This was solved, after checking the documentation, by using Django’s User.objects.create_user function.

- **Advanced Search Filters**. Ensuring that all custom filters are taken into account during advanced search, required lots of testing of different filters in isolation. At the end I landed on this solution, which, as far as I can tell, work well:

```queryset = Product.objects.filter(
            (Q(title__icontains=keyword) | Q(desc__icontains=keyword)),
            watch_brand__in=brand,
            watch_gender__in=gender,
            watch_dial_colour__in=dial_color,
            price__gte=min_price,
            price__lte=max_price,
            )
```

</details>
<br>

<br>

[&uarr; Back to Top](#heritage-company)

# Deployment

These are the steps I followed to deploy the project to Heroku:

<details>
<summary> Deployment Steps </summary>
<br>

1.  I logged in to my existing Heroku account.

2.  I clicked New and created a new app on the dashboard.

3.  I entered a unique name ('heritage-company'), selected the region (in my case, Europe), and clicked Create app.

4.  Within the created app, I selected the tab, Settings.

5.  At the Config Vars section, I clicked Reveal Config Vars.

6.  I added Config Vars (with their associated values, that I got from env.py in my IDE) for the following keys:

- `SECRET_KEY`
- `DATABASE_URL`

`DATABASE_URL` is provided by [neon.tech](https://neon.tech/) when signing up for a free database with them. On their console dashboard the necessary instructions for connecting their database to your django project should be followed exactly. As part of this process the following commands are needed to install additional libraries:

`pip3 install dj_databse_url`
`pip3 install psycopg2-binary`

Since I am using Stripe to accept payments, my Config Vars also include these keys:

- `STRIPE_ENDPOINT_SECRET`
- `STRIPE_PUBLIC_KEY`
- `STRIPE_SECRET_KEY`

The process for integrating stripe in a production environment is not straightforward. The detailed instructions in the official [Stripe documentation](https://docs.stripe.com/payments/quickstart?lang=python) should be followed exactly.

Since I am also using Amazon Web Service’s S3 buckets to store static and media files, the Heroku Config Vars also include these keys.

- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `USE_AWS` (This is set to `True`)

These keys are obtained when registering a new IAM user with Amazon Web Services. Their [official documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users.html) explains the process, and the settings.py below also reflect this integration.

Finally, for sending emails I Django I needed the following two Config Vars:

- `EMAIL_HOST_PASSWORD`
- `EMAIL_HOST_USER`

This is in line with the [Django process](https://docs.djangoproject.com/en/5.0/topics/email/#module-django.core.mail) of integrating an external SMTP (in my case, Gmail) server to send out emails.

7. Back in the Integrated Development Environment, I created a list of requirements by typing `pip3 freeze > requirements.txt` into the terminal.

8. In my Django `settings.py` file I updated/added the following settings, which are all related to deployment to Heroku:

````
DEBUG = False

ALLOWED_HOSTS = [
    ".herokuapp.com",
    "heritage-company.net",
    "www.heritage-company.net",
]

CSRF_TRUSTED_ORIGINS = [
    'https://*.herokuapp.io',
    'https://heritage-company.net'
    'https://www.heritage-company.net'
]

DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}

# Media Files - Product Images

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Email Settings / Using Gmail SMTP Server

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = 'contact@heritage-company.net'

# Stripe Settings

STRIPE_PUBLIC_KEY = os.environ.get('STRIPE_API_KEY')
STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY')
STRIPE_ENDPOINT_SECRET = os.environ.get('STRIPE_ENDPOINT_SECRET') ```

# The settings below override some other production settings to ensure that the deployed version uses AWS for static and media files storage.

if 'USE_AWS' in os.environ:

    # Use AWS for Media file storage

    # Cache control
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }

    # Bucket Config
    AWS_STORAGE_BUCKET_NAME = 'heritage-company-s3'
    AWS_S3_REGION_NAME = 'eu-central-1'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_DOMAIN_ENDING = f's3.{AWS_S3_REGION_NAME}.amazonaws.com'
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.{AWS_DOMAIN_ENDING}'
    AWS_S3_USE_SSL = True
    AWS_S3_VERIFY = True

    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'

    # Override site url in production
    SITE_URL = 'https://heritage-company.net'

````

9. I made sure to have static files (stylesheets, scripts, images etc.) available for Heroku by using the following command in the Command Line: `python manage.py collectstatic`

10. I created a Procfile for Heroku in my apps root directory. This file is simply called `Procfile` and contains the following line:

`web: gunicorn heritage.wsgi`

11. I now ensured that a working version of my code was committed and pushed to GitHub.

12. Now on Heroku again, I navigated to the Deploy tab.

13. I selected GitHub as the deployment method and connected to GitHub.

14. I searched for the repository name of the project (in my case: `code-institute-project-5`) and clicked connect.

15. I enabled automatic deploys to deploy each time new code was pushed to the repository (optional).

16. I then finally clicked Deploy Branch to deploy the project.

</details>
<br>

<br>

[&uarr; Back to Top](#heritage-company)

# Links

Deployed Website (Custom Domain): [https://heritage-company.net/](https://heritage-company.net/)<br>

Deployed Website (Alternative, Heroku Link): [https://heritage-company-386a48d92bd9.herokuapp.com/](https://heritage-company-386a48d92bd9.herokuapp.com/)<br>

Github Repository: [https://github.com/leonp84/code-institute-project-5](https://github.com/leonp84/code-institute-project-5)

# Credits

<details>
<summary> Content and Media Credits </summary>

## Media and Text

- For general project inspiration and, the Code Institute PP5 walkthrough, [Boutique Ado](https://github.com/Code-Institute-Solutions/boutique_ado_v1), provided a great starting point.
- For general visual design and site layout, I relied heavily on [The 1916 Company](https://www.the1916company.com/)
- Product images and details for fixtures, were scraped from [Crown & Caliber](https://www.crownandcaliber.com/) and [Helveti](https://www.helveti.eu/)
- Most of the images on the about us page are from [Unsplash](https://unsplash.com/)
- Logo design by [Looka](https://looka.com/)
- Some of text content on the about us page was written by [ChatGPT 4.0](https://chatgpt.com/) and then copied and adapted by myself. This is also true for the product blurb text content at the top of the product brand pages (breitling.html, tissot.html, etc)
- [Animate.css](https://animate.style/) provided the CSS for the fly-in effect of HTML elements on the landing page.
- The favicon was generated with [favicon.io](https://favicon.io/favicon-converter/)
- The site privacy policy was generated with [GDPR Privacy Notice](https://www.gdprprivacynotice.com/)
- The site terms and conditions text content were generated with [this tool](https://www.termsandconditionsgenerator.com/)

## Code and Content

- For help with custom email verification with Django (during newsletter signup): [Python in Plain English](https://python.plainenglish.io/how-to-send-email-with-verification-link-in-django-efb21eefffe8)
- For help with Customizing the Django AllAuth signup form: [Stack Overflow](https://stackoverflow.com/questions/19683179/remove-username-field-from-django-allauth)
- For help with an easy solution to show HTML error messages during form validation: [daverupert.com](https://daverupert.com/2017/11/happier-html5-forms/)
- Stack Overflow also proved very helpful with the following:
  - Filtering a Django queryset using [multiple id’s](https://stackoverflow.com/questions/9822774/filter-by-id-for-multiple-data-in-django)
  - Formatting numbers in python to use a [thousands separator](https://stackoverflow.com/questions/1823058/how-to-print-a-number-using-commas-as-thousands-separators)
  - Manually creating [new users](https://stackoverflow.com/questions/10372877/how-to-create-a-user-in-django) in Django.
  - Using the `user_passes_test` decorator to ensure only [superusers can access a view](https://stackoverflow.com/questions/12003736/django-login-required-decorator-for-a-superuser)
  - Setting some fields in a Django admin model as [read only](https://stackoverflow.com/questions/13817525/django-admin-make-all-fields-readonly)
  - Testing Django views that accept [Json Post Data](https://stackoverflow.com/questions/57989807/get-data-from-jsonresponse-in-django)
- I referenced the official [Django documentation](https://docs.djangoproject.com/en/5.0/) for too many small things to mention here.
- [ChatGPT 4.0](https://chatgpt.com/) helped with writing code to preload images using the JavaScript `new Image()` method.
- For help with testing forms with [ImageFields](https://gist.github.com/drillbits/5432699)
- For help with delaying a CSS fly in effect using the JavaScript IntersectionObserver: [CoolCSSAnimations](https://coolcssanimation.com/how-to-trigger-a-css-animation-on-scroll/)
- For help with a ‘hover off’ type effect with images: [css-tricks.com](https://css-tricks.com/different-transitions-for-hover-on-hover-off/)

</details>

<br>

[&uarr; Back to Top](#heritage-company)
