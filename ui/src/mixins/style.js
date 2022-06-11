import { style } from "@styles/variables.js";

export const styleMixin = {
  data() {
    return {
      style: {
        color: {}
      }
    };
  },
  mounted() {
    this.style = { ...this.style, ...style };
  },
  computed: {
    isMobile() {
      const isMobileBrowser =
        /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(
          navigator.userAgent
        );
      const isMobileScreen = this.windowWidth < 768;
      return isMobileScreen || isMobileBrowser;
    }
  }
};
