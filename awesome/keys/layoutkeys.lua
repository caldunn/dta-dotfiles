local awful = require('awful')
local gtable = require('gears.table')

layoutkeys = gtable.join(
  awful.key({ modkey, ctrlkey }, "l",
    function()
      awful.tag.incmwfact( 0.05)
    end,
    {description = "increase master width factor", group = "layout manipulation"}),

  awful.key({ modkey, ctrlkey }, "h",
    function()
      awful.tag.incmwfact(-0.05)
    end,
    {description = "decrease master width factor", group = "layout manipulation"}),


  awful.key({ modkey, altkey }, "k",
    function()
      awful.tag.incnmaster( 1, nil, true)
    end,
    {description = "increase the number of master clients", group = "layout manipulation"}),

  awful.key({ modkey, altkey }, "j",
    function()
      awful.tag.incnmaster(-1, nil, true)
    end,
    {description = "decrease the number of master clients", group = "layout manipulation"}),


  awful.key({ modkey, altkey }, "l",
    function()
      awful.tag.incncol( 1, nil, true)
    end,
    {description = "increase the number of columns", group = "layout manipulation"}),

  awful.key({ modkey, altkey }, "h",
    function()
      awful.tag.incncol(-1, nil, true)
    end,
    {description = "decrease the number of columns", group = "layout manipulation"}),


  awful.key({ modkey }, "space",
    function()
      awful.layout.inc( 1)
    end,
    {description = "select next", group = "layout"}),

  awful.key({ modkey, shiftkey }, "space",
    function()
      awful.layout.inc(-1)
    end,
    {description = "select previous", group = "layout"})
)
