Create data for the pricing section of the landing page with a single title for the pricing section, as well as at least 3 sample product pricing.
The data should be in pain text, with no additional formatting.
Only produce the title and pricing separated by a new line and --, nothing else.
Each price category should have at least 3 features, a name for the product level and a price for the product level.

The pricing categories should be surrounded by { and }
each category should be separated by **

Below is an example output:

    title: Pricing
    --
    categories: [
        {
            name: Basic
            **
            price: $10/month
            **
            features: [
                feature 1
                **
                feature 2
                **
                feature 3
            ]
        }
        **
        {
            name: Pro
            **
            price: $20/month
            **
            features: [
                feature 1
                **
                feature 2
                **
                feature 3
            ]
        }
        **
        {
            name: Elite
            **
            price: $30/month
            **
            features: [
                feature 1
                **
                feature 2
                **
                feature 3
            ]
        }
    ]
