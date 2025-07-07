const { createApp } = Vue


createApp({
    // Can't have a template boption since it will override the HTML template and won't render
    // the shoppingItems.
    delimiters: ['[[', ']]'],
    data() {
        return {
            message: 'Hello, Vue!',

            shoppingItems: [
            {name: 'pizza_boxes'},
            {name: 'fc_soda'},
            {name: 'fe_soda'},
            {name: 'fc_smoothie'},
            {name: 'fe_smoothie'},
            {name: 'fc_mocha'},
            {name: 'fe_mocha'},
            {name: 'kiosk_soda'},
            {name: 'kiosk_smoothie'},
            {name: 'kiosk_mocha'},
            {name: 'fc_latte'},
            {name: 'kiosk_latte'},
            {name: 'fe_latte'},
            {name: 'bake_sales'},
            {name: 'ice_cream_sales'},
            {name: 'hotdog_sales'}

            ],
        };
    }
}).mount('#app');

createApp({
    // Can't have a template boption since it will override the HTML template and won't render
    // the shoppingItems.
    delimiters: ['[[', ']]'],
    data() {
        return {
            message1: 'Hello, app2!',

            shoppingItems: [
            {name: 'pizza_boxes'},
            {name: 'fc_soda'},
            {name: 'fe_soda'},
            {name: 'fc_smoothie'},
            {name: 'fe_smoothie'},
            {name: 'fc_mocha'},
            {name: 'fe_mocha'},
            {name: 'kiosk_soda'},
            {name: 'kiosk_smoothie'},
            {name: 'kiosk_mocha'},
            {name: 'fc_latte'},
            {name: 'kiosk_latte'},
            {name: 'fe_latte'},
            {name: 'bake_sales'},
            {name: 'ice_cream_sales'},
            {name: 'hotdog_sales'}

            ],
            shopData: flask_data
        };
    }
}).mount('#app2');
