module.exports = {
  purge: [],
  darkMode: false, // or 'media' or 'class'
  theme: {
    fontFamily: {
      'sans': ['Niramit', 'Sans-serif']
    },
    extend: {
      colors:{
        logo:'#f0454d',
      },
      spacing:{
        // 왼쪽은 클래스 이름, 오른쪽은 CSS를 위한 것 
        "25vh":"25vh", 
        "50vh":"50vh",
        "75vh":"75vh",  
      },
      borderRadius:{
        xl: "1.5rem"
      },
      minHeight:{
        "50vh":"50vh",
        "75vh":"75vh"
      }
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
};
