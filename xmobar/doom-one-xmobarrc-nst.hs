-- Xmobar (http://projects.haskell.org/xmobar/)
-- This is one of the xmobar configurations for DTOS.
-- This config is packaged in the DTOS repo as 'dtos-xmobar'
-- Color scheme: Doom One
-- Dependencies: 
   -- otf-font-awesome 
   -- ttf-mononoki 
   -- ttf-ubuntu-font-family
   -- htop
   -- emacs
   -- pacman (Arch Linux)
   -- trayer
   -- 'dtos-local-bin' (from dtos-core-repo)

-- etemplate = "abc" ++ "123"

Config { font            = "xft:Ubuntu:weight=bold:pixelsize=11:antialias=true:hinting=true"
       , additionalFonts = [ "xft:Mononoki:pixelsize=11:antialias=true:hinting=true"
                           , "xft:Font Awesome 6 Free Solid:pixelsize=12"
                           , "xft:Font Awesome 6 Brands:pixelsize=12"
                           ]
       , bgColor      = "#282c34"
       , fgColor      = "#ff6c6b"
       -- Position TopSize and BottomSize take 3 arguments:
       --   an alignment parameter (L/R/C) for Left, Right or Center.
       --   an integer for the percentage width, so 100 would be 100%.
       --   an integer for the minimum pixel height for xmobar, so 24 would force a height of at least 24 pixels.
       --   NOTE: The height should be the same as the trayer (system tray) height.
       , position       = TopSize L 100 24
       , lowerOnStart = True
       , hideOnStart  = False
       , allDesktops  = True
       , persistent   = True
       , iconRoot     = ".xmonad/xpm/"  -- default: "."
       , commands = [
                        -- Echos a "penguin" icon in front of the kernel output.
                      Run Com "echo" ["<fn=3>\xf17c</fn>"] "penguin" 3600
                        -- Get kernel version (script found in .local/bin)
                    , Run Com "uname" ["-r"] "kernal" 36000
                        -- Cpu usage in percent
                    , Run Cpu ["-t", "<fn=2>\xf108</fn>  CPU: (<total>%)","-H","50","--high","red"] 20
                        -- Ram used number and percent
                    , Run Memory ["-t", "<fn=2>\xf233</fn>  MEM: <used>M (<usedratio>%)"] 20
                        -- Disk space free
                    , Run DiskU [("/", "<fn=2>\xf0c7</fn>  HDD: <free> free")] [] 60
                        -- Echos an "up arrow" icon in front of the uptime output.
                    , Run Com "echo" ["<fn=2>\xf0aa</fn>"] "uparrow" 3600
                        -- Uptime
                    , Run Uptime ["-t", "uptime: <days>d <hours>h"] 360
                        -- Echos a "bell" icon in front of the pacman updates.
                    , Run Com "echo" ["<fn=2>\xf0f3</fn>"] "bell" 3600
                        -- Check for pacman updates (script found in .local/bin)
                    , Run Com ".config/xmobar/checkupdates.sh" [] "pacupdate" 36000
                        -- Echos a "battery" icon in front of the pacman updates.
                    , Run BatteryP ["BAT0"] ["-t", "<acstatus><watts> (<left>%)"] 360
                        -- Time and date
                    , Run Date "<fn=2>\xf017</fn>  %b %d %Y - (%H:%M) " "date" 50
                        -- Script that dynamically adjusts xmobar padding depending on number of trayer icons.
                    , Run Com ".config/xmobar/trayer-padding-icon.sh" [] "trayerpad" 20
                        -- Prints out the left side items such as workspaces, layout, etc.
                    , Run UnsafeStdinReader

                    , Run Weather "YPPH" ["-t", "<station>: <tempC>C"] 36000
                    ]
       , sepChar = "%"
       , alignSep = "}{"
       , template = " <action=`dmenu_run`><icon=haskell_20.xpm/> </action> <fc=#666666>|</fc> %UnsafeStdinReader% }{ <box type=Bottom width=2 mb=2 color=#51afef><fc=#51afef>%penguin%  %kernal%</fc></box>  <box type=Bottom width=2 mb=2 color=#ecbe7b><fc=#ecbe7b><action=`kitty -e htop`>%cpu%</action></fc></box>    <box type=Bottom width=2 mb=2 color=#ff6c6b><fc=#ff6c6b><action=`alacritty -e htop`>%memory%</action></fc></box>    <box type=Bottom width=2 mb=2 color=#a9a1e1><fc=#a9a1e1>%disku%</fc></box>    <box type=Bottom width=2 mb=2 color=#98be65><fc=#98be65>%uparrow%  %uptime%</fc></box>    <box type=Bottom width=2 mb=2 color=#c678dd><fc=#c678dd>%bell%  <action=`kitty -e sudo pacman -Syu`>%pacupdate%</action></fc></box>    <box type=Bottom width=2 mb=2 color=#51afef><fc=#51afef>%YPPH%</fc></box>    <box type=Bottom width=2 mb=2 color=#46d9ff><fc=#46d9ff><action=`kitty`>%date%</action></fc></box>" 
       }
