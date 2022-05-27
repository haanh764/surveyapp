<template>
  <v-list-item class="mb-0 justify-space-between pl-3">
    <v-list-item-avatar>
      <span>
        {{ userData.email[0] || "e" }}
      </span>
    </v-list-item-avatar>

    <v-list-item-content class="pl-2">
      <v-list-item-title class="text-body">
        {{ userData.email || "email@email.com" }} 
      </v-list-item-title>
    </v-list-item-content>
  </v-list-item>
</template>

<script>
import { get } from "vuex-pathify";

export default {
  name: "DefaultDrawerHeader",
  computed: { 
    userData() {
      const defaultUserData = {email: ""};
      return {...defaultUserData, ...get("user/userData")};
    } 
  }
};
</script>
