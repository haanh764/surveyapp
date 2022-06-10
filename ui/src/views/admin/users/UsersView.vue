<template>
  <v-container
    id="admin-users-view"
    class="admin-users-view"
    tag="section"
  >
    <v-row justify="center">
      <v-col :cols="isMobile? 12 : 10">
        <v-card
          class="admin-users-card text-center"
          elevation="2"
          :class="{'--is-mobile': isMobile, '--is-desktop': !isMobile}"
        >
          <v-row justify="center">
            <v-col cols="12">
              <!-- USERS DATATABLE STARTS HERE : MOBILE -->
              <template v-if="isMobile">
                <v-row justify="center">
                  <v-col cols="9" class="mb-2">
                    <v-text-field
                      v-model.trim="keyword"
                      solo
                      dense
                      height="48"
                      class="admin-users-search"
                      label="Search user by email"
                      append-icon="mdi-magnify"
                    />
                    <p class="text-left text-secondary">
                      {{ users.length }} users
                    </p>
                  </v-col>
                  <v-col cols="3" class="text-right">
                    <v-btn
                      text
                      icon
                      elevation="2"
                      height="48"
                      width="48"
                      class="v-btn--default"
                      @click="isSortedAscending = !isSortedAscending"
                    >
                      <v-icon>
                        {{ isSortedAscending ? 'mdi-sort-alphabetical-ascending' : 'mdi-sort-alphabetical-descending' }}
                      </v-icon>
                    </v-btn>
                  </v-col>
                </v-row>
                <v-list>
                  <v-list-item
                    v-for="user in filteredUsers"
                    :key="user.id"
                    cols="12"
                    class="pa-0"
                  >
                    <v-list-item-content class="pa-2 pb-4">
                      <v-row justify="space-between">
                        <v-col
                          cols="auto"
                          align-self="start"
                        >
                          <h2 class="mb-1">
                            {{ user.email }}
                          </h2>
                        </v-col>
                      </v-row>
                      <v-divider />
                    </v-list-item-content>
                  </v-list-item>
                </v-list>
              </template>
              <!-- USERS DATATABLE ENDS HERE : MOBILE -->
              <!-- USERS DATATABLE STARTS HERE : DESKTOP -->
              <template v-else>
                <v-row
                  justify="start"
                  class="mb-2"
                >
                  <v-col
                    cols="7"
                    class="text-left"
                  >
                    <h1>
                      Users
                    </h1>
                  </v-col>
                </v-row>
                <v-data-table
                  :headers="tableHeaders"
                  :items="filteredUsers"
                  item-key="name"
                  class="elevation-1 admin-users-table"
                  :search="keyword"
                >
                  <template #top>
                    <v-row
                      justify="start"
                      class="admin-users-table__top"
                    >
                      <v-col cols="auto">
                        <v-text-field
                          v-model.trim="keyword"
                          solo
                          dense
                          class="admin-users-search --is-desktop"
                          prepend-inner-icon="mdi-magnify"
                          label="Search user by email"
                        />
                      </v-col>
                    </v-row>
                  </template>
                  <template #item.isActivated="{ item }">
                    <v-chip
                      small
                      :color="getIsActivatedStatus(item.isActivated).color"
                      :text-color="getIsActivatedStatus(item.isActivated).textColor"
                    >
                      {{ getIsActivatedStatus(item.isActivated).text }}
                    </v-chip>
                  </template>
                  <template #item.isBlocked="{ item }">
                    <v-chip
                      small
                      :color="getIsBlockedStatus(item.isBlocked).color"
                      :text-color="getIsBlockedStatus(item.isBlocked).textColor"
                    >
                      {{ getIsBlockedStatus(item.isBlocked).text }}
                    </v-chip>
                  </template>
                  <template #item.id="{item}">
                    <v-row justify="space-between">
                      <v-col cols="12">
                        <v-btn
                          text
                          icon
                          elevation="1"
                          small
                          class="v-btn--default mr-2"
                          @click="onClickItemEdit(item)"
                        >
                          <v-icon small>
                            mdi-pencil
                          </v-icon>
                        </v-btn>

                        <v-btn
                          text
                          icon
                          elevation="1"
                          small
                          class="v-btn--default"
                          @click="onClickItemDelete(item)"
                        >
                          <v-icon small>
                            mdi-delete
                          </v-icon>
                        </v-btn>
                      </v-col>
                    </v-row>
                  </template>
                </v-data-table>
              </template>
              <!-- USERS DATATABLE ENDS HERE : DESKTOP -->
              <modal
                v-model="isDeleteItemModalShown"
                name="delete-modal"
                title="Delete"
                content="Are you sure you want to delete this user? This action cannot be undone."
                primary-action-button-text="OK"
                @click:primary-action="onDeleteConfirmation"
              />
            </v-col>
          </v-row>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { get, sync } from "vuex-pathify";
import { mapGetters } from "vuex";
import { getUsers } from "@api";

export default {
  name: "AdminUsersView",
  data() {
    return {
      keyword: "",
      isSortedAscending: true,
      isDeleteItemModalShown: false,
      selectedUser: {},
      users: [
        {
          id: 1,
          email: "ayam@bebek.angsa",
          isActivated: 1,
          isBlocked: 0,
        },
        {
          id: 2,
          email: "sadBoy123@pevuer.pl",
          isActivated: 0,
          isBlocked: 1,
        },
        {
          id: 3,
          email: "lifeIsHard456@gmail.pl",
          isActivated: 1,
          isBlocked: 1,
        },
      ],
    };
  },
  computed: {
    ...get("user", ["userData"]),
    ...sync("app", ["mini"]),
    ...mapGetters("user", ["hasAcceptedPrivacyPolicy", "hasAcceptedTnC"]),
    filteredUsers() {
      let users = this.keyword
        ? this.users.filter((user) => {
            return user.email.toLowerCase().includes(this.keyword);
          })
        : this.users;
      return users.sort((a, b) => {
        return this.isSortedAscending
          ? a.email.localeCompare(b.email)
          : b.email.localeCompare(a.email);
      });
    },
    tableHeaders() {
      return [
        { text: "Email Address", value: "email" },
        { text: "Is Activated?", value: "isActivated" },
        { text: "Is Blocked?", value: "isBlocked" },
        { text: "Actions", value: "id" },
      ];
    },
  },
  created() {
    // get user api
    // add certain columns to user data
    this.processUserData();
  },
  mounted() {},
  methods: {
    onDeleteConfirmation() {
      // call delete api
      // delete
      // refresh table
      // hide modal
      this.isDeleteItemModalShown = false;
    },
    onClickItemDelete(item) {
      this.selectedUser = { ...item };
      this.isDeleteItemModalShown = true;
    },
    onClickItemEdit(item) {
      //show modal with toggle for activation,
      //toggle for blocking,
      //button for sending reset password link
      console.log(item);
    },
    processUserData() {
      this.users = this.users.map((user, index) => {
        return {
          ...user,
          ...{
            index,
          },
        };
      });
    },
    getIsActivatedStatus(itemStatus) {
      let item = {};
      switch (itemStatus) {
        case 1:
          item = { color: "#ffffff", text: "Active", textColor: "#000000" };
          break;
        default:
          item = { color: "#ffddb3", text: "Inactive", textColor: "#fb8c00" };
          break;
      }
      return item;
    },
    getIsBlockedStatus(itemStatus) {
      let item = {};
      switch (itemStatus) {
        case 0:
          item = { color: "#ffffff", text: "Unblocked", textColor: "#000000" };
          break;
        default:
          item = { color: "#ffb3b3", text: "Blocked", textColor: "#ff5252" };
          break;
      }
      return item;
    },
    getUserApi() {
      // example of fetching api directly with fetch
      fetch("http://localhost:8000")
        .then((response) => response.json())
        .then((data) => {
          this.message = data.message;
        })
        .catch((error) => {
          console.log(error);
        });

      // example 1 with axios
      this.$axios
        .get("https://api.coindesk.com/v1/bpi/currentprice.json")
        .then((response) => {
          if (response.status == 200) {
            // do something
          } else {
            // error
            // do something
          }
        })
        .catch((error) => {
          // do something on error
          console.error(error);
        });

      // example 2
      // recommended because this way the api is centered in one place/file
      // dont forget to handle errors
      getUsers()
        .then((response) => {
          console.log(response);
          // do something with the response
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style lang="scss">
.admin-users-view {
  margin: 20px 0;

  &.--no-padding {
    *[class~="col"] {
      padding: 0;
    }
  }
}

.admin-users-card {
  padding: 20px 0 40px;

  &.--is-mobile {
    box-shadow: none !important;
  }

  &.--is-desktop {
    box-shadow: none !important;
    background: none !important;
  }
}

.admin-users-table {
  &__top {
    background-color: $light-blue;
    margin: 0;
    overflow: hidden;
  }

  .v-data-table-header {
    background-color: $light-blue;

    th[role="columnheader"] {
      text-transform: uppercase;

      > span {
        font-weight: 600;
      }
    }
  }
}

.admin-users-search {
  &.--is-desktop {
    .v-input__slot {
      box-shadow: none !important;
      border: 1px solid $light-gray;
    }
  }
}
</style>
