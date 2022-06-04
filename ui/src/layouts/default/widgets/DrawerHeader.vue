<template>
  <div class="drawer-header">
    <v-list-item class="mb-0 justify-space-between drawer-header__list-item">
      <v-img
        v-if="!mini"
        :src="require('@assets/svg/profile_picture.svg')"
        max-height="40"
        max-width="40"
      />
      <v-list-item-avatar
        v-if="mini"
        class="drawer-header__avatar"
      >
        <span class="email">
          {{ email[0] }}
        </span>
      </v-list-item-avatar>

      <v-list-item-content class="pl-2">
        <v-list-item-title class="text-body">
          {{ email }}
        </v-list-item-title>
      </v-list-item-content>
    </v-list-item>
  </div>
</template>

<script>
import { get } from "vuex-pathify";

export default {
  name: "DefaultDrawerHeader",
  computed: {
    ...get("user", [ "userData" ]),
    ...get("app", [ "mini" ]),
    email() {
      return this.userData.email || "email@email.com";
    }
  }
};
</script>


<style scoped lang="scss">
.drawer-header {
  margin: 20px 0;

  &__list-item {
    display: flex;
    flex-flow: column;
  }

  &__avatar {
    justify-content: center;
    color: $white;
    background-color: $black;
  }

  .v-list-item__title {
    font-weight: 500;
  }
}
</style>
