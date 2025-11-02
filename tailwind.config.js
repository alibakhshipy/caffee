/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./public/*.html",'./public/pages/*.html'],
  darkMode:["class"],
  theme: {
    extend: {
      colors:{
        brown:{
          "100" : "#ECE0D1",
          "300" : "#DBC1AC",
          "600" : "#967259",
          "900" : "#634832",
        }
      },
      boxShadow:{
        "Normal" : "0px 1px 10px 0px rgba(0, 0, 0, 0.05)"
      },
      borderRadius:{
        "4xl" : "2rem"
      },
      fontFamily:{
        "DanaRegular" : "Dana Regular",
        "DanaMedium" : "Dana Medium",
        "DanaDemiBold" : "Dana DemiBold",
        "MorabbaLight" : "Morabba Light",
        "MorabbaMedium" : "Morabba Medium",
        "MorabbaBold" : "Morabba Bold",
      },
      letterSpacing:{
        "tightest" : "-0.065em"
      },
      container:{
        center:true,
        padding:{
          DEFAULT: "1rem",
          lg: "0.625rem"
        }
      },
      backgroundImage:{
        "home-desktop" : "url(../image/headerBgDesktop.webp)",
        "home-mobile" : "url(../image/headerBgMobile.webp)",

      }
    },
    screens:{
      "xss":"340px",
      'xs':'480px',
      'sm': '640px',
      'md': '768px',
      'lg': '1024px',
      'lgn':'1152px',
      'xl': '1280px',
    }
  },
  plugins: [
    function({addVariant}){
      addVariant("child", "& > *");
      addVariant("child-hover", "& > *:hover");

    }
  ],
}

module.exports = {
  content: [
    "./templates/**/*.{html,js}",
    "./**/templates/**/*.{html,js}",
    "./static/**/*.{js,css}"
  ],
  theme: {
    extend: {},
  },
  darkMode: 'class',
  plugins: [
    require('@tailwindcss/typography'),
  ],
}
