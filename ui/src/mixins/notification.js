import { VSnackbar, VBtn } from "vuetify/lib";

export const notificationMixin = {
  provide() {
    return { child: this };
  },
  components: {
    notification: {
      inject: [ "child" ],
      components: { VSnackbar, VBtn },
      template: `
        <div class="snackbar-notification" >
          <v-snackbar
            ref="snackbarNotification"
            right
            top
            :color="child.notificationOptions.color"
            :value="true"
          >
            {{ child.notificationMessage }}
            
            <template v-slot:action="{ attrs }">
              <v-btn
                color="white"
                text
                v-bind="attrs"
                @click="child.isNotificationShown = false"
              >
                Close
              </v-btn>
            </template>

          </v-snackbar>
        </div>
      `
    }
  },
  data() {
    return {
      notificationMessage: "Notification",
      notificationOptions: {
        color: "success" // success, info, success etc is also possible
      },
      isNotificationShown: false
    };
  },
  methods: {
    hideNotification() {
      this.child.isNotificationShown = false;
    },
    showNotification(message = "", options = {}) {
      this.notificationMessage = message;
      this.notificationOptions = { ...this.notificationOptions, ...options };
      this.isNotificationShown = true;
    }
  }
};
