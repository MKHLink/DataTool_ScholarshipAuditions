import { extendTheme } from "@chakra-ui/react";

const theme = extendTheme({
  colors: {
    primary: {
        50: "#f7f7f7",
        100: "#eaeaea",
        200: "#d4d4d4",
        300: "#bfbfbf",
        400: "#a9a9a9",
        500: "#949494",
        600: "#7e7e7e",
        700: "#696969",
        800: "#535353",
        900: "#3e3e3e",
      },
      secondary: {
        50: "#f0f0f0",
        100: "#dddddd",
        200: "#c9c9c9",
        300: "#b5b5b5",
        400: "#a1a1a1",
        500: "#8d8d8d",
        600: "#7a7a7a",
        700: "#666666",
        800: "#525252",
        900: "#3e3e3e",
      },
  },
});

export default theme;
