// The Deal Sifter feed. This file is the only thing the scheduled refresh rewrites.
// verdict: "buy" | "wait" | "shit".  kind: "deal" (a specific offer) | "trap" (a pattern to avoid).
// price/was are numbers in USD or null. priceText is shown when price is null.
window.DEALS = {
  updated: "2026-11-14T11:50:00-05:00",
  stat: {
    text: "One analysis of Black Friday 2024 found about 3 in 4 tech discounts on two big US marketplaces were suspect.",
    source: { name: "TechRadar Pro", url: "https://techradar.com/pro/tech-deals-in-2025-navigating-ghost-discounts-and-fake-reviews" }
  },
  deals: [
    {
      id: "lg-c6-55", verdict: "buy", kind: "deal", cat: "TVs",
      name: "LG C6 55-inch OLED TV", price: 999.99, was: 1599.99, store: "Amazon, Best Buy",
      why: "About 38% under list, on the set TechRadar named its TV of the year. A real model, not a doorbuster variant.",
      instead: null, confidence: "high", checked: "2026-11-14",
      source: { name: "Tom's Guide", url: "https://www.tomsguide.com/live/news/black-friday-2026-live-deals-and-more" }
    },
    {
      id: "ring-doorbell-2k", verdict: "buy", kind: "deal", cat: "Smart home",
      name: "Ring Battery Doorbell 2K", price: 39, was: 100, store: "Amazon",
      why: "Tom's Guide tracks this as the lowest price it has ever hit.",
      instead: null, confidence: "high", checked: "2026-11-14",
      source: { name: "Tom's Guide", url: "https://www.tomsguide.com/live/news/black-friday-2026-live-deals-and-more" }
    },
    {
      id: "bose-flex-2", verdict: "buy", kind: "deal", cat: "Audio",
      name: "Bose SoundLink Flex (2nd gen) speaker", price: 99, was: null, store: "See source",
      why: "Reported as an all-time low for a speaker that rarely drops under $119.",
      instead: null, confidence: "medium", checked: "2026-11-14",
      source: { name: "Tom's Guide", url: "https://www.tomsguide.com/live/news/black-friday-2026-live-deals-and-more" }
    },
    {
      id: "ninja-crispi", verdict: "buy", kind: "deal", cat: "Kitchen",
      name: "Ninja Crispi air fryer", price: 89, was: null, store: "Walmart",
      why: "CNN Underscored puts this within $4 of the price it expects on Black Friday itself. Walmart's early event ends Nov 15.",
      instead: null, confidence: "medium", checked: "2026-11-14",
      source: { name: "CNN Underscored", url: "https://www.cnn.com/cnn-underscored/deals/best-black-friday-deals-2026-11-09" }
    },
    {
      id: "ninja-bn701", verdict: "buy", kind: "deal", cat: "Kitchen",
      name: "Ninja Professional Plus blender (BN701)", price: 79.99, was: 119.99, store: "Amazon",
      why: "Ties its lowest price of 2026.",
      instead: null, confidence: "high", checked: "2026-11-14",
      source: { name: "Popular Science", url: "https://www.popsci.com/gear/amazon-early-black-friday-deals-2026-year-lows/" }
    },
    {
      id: "philips-2300", verdict: "buy", kind: "deal", cat: "Kitchen",
      name: "Philips 2300 espresso machine with LatteGo", price: 499.99, was: 699.99, store: "Amazon",
      why: "Ties its lowest price of 2026. $200 off a machine that holds its price most of the year.",
      instead: null, confidence: "high", checked: "2026-11-14",
      source: { name: "Popular Science", url: "https://www.popsci.com/gear/amazon-early-black-friday-deals-2026-year-lows/" }
    },
    {
      id: "lodge-chef-3", verdict: "buy", kind: "deal", cat: "Kitchen",
      name: "Lodge Chef Collection cast-iron skillets, set of 3", price: 64, was: 90, store: "Lodge",
      why: "Lodge rarely discounts. $26 off three pans that last decades.",
      instead: null, confidence: "medium", checked: "2026-11-14",
      source: { name: "CNN Underscored", url: "https://www.cnn.com/cnn-underscored/deals/best-black-friday-deals-2026-11-09" }
    },
    {
      id: "skil-drill", verdict: "buy", kind: "deal", cat: "Tools",
      name: "Skil PWR Core 20 brushless compact drill kit", price: 79.99, was: 109, store: "Amazon",
      why: "Its lowest price of 2026.",
      instead: null, confidence: "high", checked: "2026-11-14",
      source: { name: "Popular Science", url: "https://www.popsci.com/gear/amazon-early-black-friday-deals-2026-year-lows/" }
    },
    {
      id: "craftsman-v20-59", verdict: "buy", kind: "deal", cat: "Tools",
      name: "Craftsman V20 drill or impact driver kit", price: 59, was: null, store: "Lowe's",
      why: "$59 each in store, flagged by a tool reviewer who bought and tested them. No price history to check it against.",
      instead: null, confidence: "medium", checked: "2026-11-14",
      source: { name: "731 Woodworks", url: "https://www.731woodworks.com/731-blog/early-black-friday-tool-deals-at-lowes" }
    },
    {
      id: "ring-floodlight", verdict: "buy", kind: "deal", cat: "Smart home",
      name: "Ring Floodlight Cam 2K (wired)", price: 99.99, was: 199.99, store: "Amazon",
      why: "Half off, tying its lowest price of 2026.",
      instead: null, confidence: "high", checked: "2026-11-14",
      source: { name: "Popular Science", url: "https://www.popsci.com/gear/amazon-early-black-friday-deals-2026-year-lows/" }
    },
    {
      id: "lego-10698", verdict: "buy", kind: "deal", cat: "Toys",
      name: "LEGO Classic Large Creative Brick Box (10698)", price: null, priceText: "44% off", was: null, store: "Amazon",
      why: "A staple set that usually gets 20% at best. One smaller source reported this, so confirm the price before buying.",
      instead: null, confidence: "low", checked: "2026-11-14",
      source: { name: "Smart Value Choice", url: "https://smartvaluechoice.com/early-black-friday-deals/" }
    },

    {
      id: "lg-c6-65", verdict: "wait", kind: "deal", cat: "TVs",
      name: "LG C6 65-inch OLED TV", price: 1399.99, was: 2699.99, store: "Amazon",
      why: "Billed as a record low, but it has sat at $1,400 to $1,500 for weeks. The real saving is about $100.",
      instead: "Hold for $1,249 or less, or take the 55-inch at $999.99 now.",
      confidence: "medium", checked: "2026-11-14",
      source: { name: "DigitBin", url: "https://www.digitbin.com/best-black-friday-tv-deals-2026/" }
    },
    {
      id: "tcl-qm8l-65", verdict: "wait", kind: "deal", cat: "TVs",
      name: "TCL QM8L 65-inch Mini LED TV", price: 1197.99, was: 2499.99, store: "Amazon",
      why: "The 52% off is measured against a launch price nobody pays. It already sold for about $1,078 this month.",
      instead: "Good TV, wrong price. Wait for $999 or less.",
      confidence: "medium", checked: "2026-11-14",
      source: { name: "DigitBin", url: "https://www.digitbin.com/best-black-friday-tv-deals-2026/" }
    },

    {
      id: "outlet-wristlet", verdict: "shit", kind: "deal", cat: "Style",
      name: "Kate Spade Outlet Lucy wristlet", price: 29, was: 139, store: "Kate Spade Outlet",
      why: "The 79% off is against an outlet reference price. Outlet stores run discounts like this all year, so $29 is close to the normal price.",
      instead: "Fine if you want a $29 wristlet. Just don't buy it for the discount.",
      confidence: "medium", checked: "2026-11-14",
      source: { name: "Yahoo Shopping", url: "https://shopping.yahoo.com/deals/breaking-news/article/black-friday-2026-early-deals-from-kate-spade-dyson-hoka-and-more-plus-everything-we-know-so-far-about-the-big-sale-155240970.html" }
    },
    {
      id: "trap-60-70-tv", verdict: "shit", kind: "trap", cat: "TVs",
      name: "Any 60-inch or 70-inch doorbuster TV", price: null, priceText: "Usually $250 to $450", was: null, store: "Everywhere",
      why: "Good TV lines come in 55, 65, 75 and 85 inches. A 60 or 70 is almost always the brand's bottom-tier panel wearing a big number.",
      instead: "A 55 or 65-inch from a line reviewers have tested. The 55 often costs about the same.",
      confidence: "high", checked: "2026-11-14",
      source: { name: "Tom's Guide", url: "https://www.tomsguide.com/tvs/im-a-tv-expert-dont-make-these-5-tv-shopping-mistakes-this-black-friday" }
    },
    {
      id: "trap-derivative", verdict: "shit", kind: "trap", cat: "TVs",
      name: "TVs and laptops with a model number you can't find reviewed", price: null, priceText: "Headline price", was: null, store: "Big-box doorbusters",
      why: "Brands build stripped-down versions just to hit a Black Friday price. Fewer ports, dimmer panel, slower chip, familiar logo.",
      instead: "Search the exact model number. No reviews from before November means skip it.",
      confidence: "high", checked: "2026-11-14",
      source: { name: "Sharp Finds", url: "https://www.getsharpfinds.com/blog/black-friday-2026-what-to-buy-what-to-skip" }
    },
    {
      id: "trap-mattress", verdict: "shit", kind: "trap", cat: "Home",
      name: "Mattress 'biggest sale of the year'", price: null, priceText: "30% to 50% off", was: null, store: "Online mattress brands",
      why: "Mattresses are on sale every week of the year. The Black Friday price is the Tuesday-in-March price.",
      instead: "Buy when you need one. Compare the final price across brands, not the percentage.",
      confidence: "high", checked: "2026-11-14",
      source: { name: "Sharp Finds", url: "https://www.getsharpfinds.com/blog/black-friday-2026-what-to-buy-what-to-skip" }
    },
    {
      id: "trap-watches", verdict: "shit", kind: "trap", cat: "Style",
      name: "Watches and jewelry at 60% to 80% off", price: null, priceText: "Off an inflated MSRP", was: null, store: "Department stores, Amazon",
      why: "The crossed-out price is a number the piece never sold at. Judge it by what it costs the rest of the year.",
      instead: "Pick the piece first, then check its price over the last 90 days.",
      confidence: "high", checked: "2026-11-14",
      source: { name: "Sharp Finds", url: "https://www.getsharpfinds.com/blog/black-friday-2026-what-to-buy-what-to-skip" }
    }
  ]
};
