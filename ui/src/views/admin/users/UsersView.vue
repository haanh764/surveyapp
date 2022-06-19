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
                  <v-col
                    cols="9"
                    class="mb-2"
                  >
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
                  <v-col
                    cols="3"
                    class="text-right"
                  >
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
                title="Delete Account"
                content="Are you sure you want to DELETE this user account? This action cannot be undone."
                primary-action-button-text="OK"
                @click:primary-action="onDeleteConfirmation"
              />

              <modal
                v-model="isEditItemModalShown"
                name="edit-modal"
                :is-footer-shown="false"
              >
                <template #default>
                  <v-card-title>
                    <p class="mb-10">
                      Manage User
                    </p>
                  </v-card-title>
                  <v-col
                    cols="auto"
                    class="py-0 px-8"
                  >
                    <v-row
                      justify="center"
                      align="center"
                    >
                      <v-col
                        cols="7"
                        class="py-0"
                      >
                        <p class="edit-modal__action-title">
                          Activate Account
                        </p>
                        <p class="edit-modal__action-description">
                          Activate account after registration to enable
                          the user to use the whole website features.
                        </p>
                      </v-col>
                      <v-col
                        cols="5"
                        class="py-0"
                      >
                        <v-btn
                          text
                          class="edit-modal__action-button"
                          :class="isSelectedUserActivated? 'v-btn--disabled' : 'v-btn--primary'"
                          :disabled="isSelectedUserActivated"
                          height="35"
                          block
                          @click="onClickSelectedUserActivate"
                        >
                          ACTIVATE ACCOUNT
                        </v-btn>
                      </v-col>
                    </v-row>
                    <v-row
                      justify="center"
                      align="center"
                    >
                      <v-col
                        cols="7"
                        class="py-0"
                      >
                        <p class="edit-modal__action-title">
                          Block Account
                        </p>
                        <p class="edit-modal__action-description">
                          Block/unblock account to limit/allow website usage.
                        </p>
                      </v-col>
                      <v-col
                        cols="5"
                        class="py-0"
                      >
                        <v-row justify="center">
                          <v-switch
                            v-model="selectedUser.isBlocked"
                            @click.native.stop="toggleSelectedUserIsBlocked"
                          />
                        </v-row>
                      </v-col>
                    </v-row>
                    <v-row
                      justify="center"
                      align="center"
                    >
                      <v-col
                        cols="7"
                        class="py-0"
                      >
                        <p class="edit-modal__action-title">
                          Reset Password
                        </p>
                        <p class="edit-modal__action-description">
                          Send a new password to the associated email address.
                        </p>
                      </v-col>
                      <v-col
                        cols="5"
                        class="py-0"
                      >
                        <v-btn
                          text
                          class="v-btn--primary edit-modal__action-button"
                          height="35"
                          block
                          @click="onClickSelectedUserResetPassword"
                        >
                          RESET PASSWORD
                        </v-btn>
                      </v-col>
                    </v-row>
                    <v-row justify="end">
                      <v-btn
                        text
                        class="text-none mt-2 mb-5 edit-modal__close-button"
                        :color="style.color.primary"
                        height="40"
                        @click="onClickCloseEditModal()"
                      >
                        CLOSE
                      </v-btn>
                    </v-row>
                  </v-col>
                </template>
              </modal>

              <modal
                v-model="isAccountActivationModalShown"
                name="account-activation-modal"
                title="Activate Account"
                content="Are you sure you want to ACTIVATE this user's account? This action cannot be undone."
                primary-action-button-text="OK"
                @click:primary-action="onAccountActivationConfirmation"
              />

              <modal
                v-model="isAccountBlockModalShown"
                name="account-block-modal"
                :is-close-button-shown="false"
                :is-footer-shown="false"
              >
                <template #default>
                  <v-card-title>
                    <p class="mb-10">
                      Block Account
                    </p>
                  </v-card-title>
                  <v-card-text>
                    Are you sure you want to BLOCK this user's account?
                  </v-card-text>
                  <v-card-actions>
                    <v-row justify="end">
                      <v-col
                        cols="auto"
                        class="text-right"
                      >
                        <v-btn
                          text
                          class="text-uppercase"
                          @click.stop="onAccountBlockCancelation"
                        >
                          CANCEL
                        </v-btn>
                        <v-btn
                          color="primary"
                          text
                          class="text-uppercase"
                          @click="onAccountBlockConfirmation"
                        >
                          OK
                        </v-btn>
                      </v-col>
                    </v-row>
                  </v-card-actions>
                </template>
              </modal>

              <modal
                v-model="isAccountUnblockModalShown"
                name="account-unblock-modal"
                :is-close-button-shown="false"
                :is-footer-shown="false"
              >
                <template #default>
                  <v-card-title>
                    <p class="mb-10">
                      Unblock Account
                    </p>
                  </v-card-title>
                  <v-card-text>
                    Are you sure you want to UNBLOCK this user's account?
                  </v-card-text>
                  <v-card-actions>
                    <v-row justify="end">
                      <v-col
                        cols="auto"
                        class="text-right"
                      >
                        <v-btn
                          text
                          class="text-uppercase"
                          @click.stop="onAccountUnblockCancelation"
                        >
                          CANCEL
                        </v-btn>
                        <v-btn
                          color="primary"
                          text
                          class="text-uppercase"
                          @click="onAccountUnblockConfirmation"
                        >
                          OK
                        </v-btn>
                      </v-col>
                    </v-row>
                  </v-card-actions>
                </template>
              </modal>

              <modal
                v-model="isResetPasswordModalShown"
                name="reset-password-modal"
                title="Reset Password"
                content="Are you sure you want to RESET this user's password? This action cannot be undone."
                primary-action-button-text="OK"
                @click:primary-action="onResetPasswordConfirmation"
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
import {
  adminListUsers, adminResetUserPassword, adminActivateUser,
  adminBlockUser, adminUnblockUser, adminDeleteUser
} from "@api";

export default {
  name: "AdminUsersView",
  data() {
    return {
      keyword: "",
      isSortedAscending: true,
      isEditItemModalShown: false,
      isDeleteItemModalShown: false,
      isAccountActivationModalShown: false,
      isAccountBlockModalShown: false,
      isAccountUnblockModalShown: false,
      isResetPasswordModalShown: false,
      selectedUser: {},
      users: []
    };
  },
  computed: {
    ...get("user", [ "userData" ]),
    ...sync("app", [ "mini" ]),
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
        { text: "Activation Status", value: "isActivated" },
        { text: "Blockade Status", value: "isBlocked" },
        { text: "Actions", value: "id" }
      ];
    },
    isSelectedUserActivated() {
      if (this.selectedUser.isActivated == 1) {
        return true;
      }
      return false;
    }
  },
  created() {
    this.getUsersApi();
    this.processUserData();
  },
  mounted() {},
  methods: {
    onClickItemDelete(item) {
      this.selectedUser = { ...item };
      this.isDeleteItemModalShown = true;
    },
    onDeleteConfirmation() {
      const apiData = { email: this.selectedUser.email };
      adminDeleteUser(apiData).then((response) => {
        this.$notify.toast(response["message"]);
        this.getUsersApi();
        this.processUserData();
      });
      this.isDeleteItemModalShown = false;
    },
    onClickCloseEditModal() {
      this.isEditItemModalShown = false;
    },
    onClickItemEdit(item) {
      this.selectedUser = { ...item };
      this.isEditItemModalShown = true;
    },
    onClickSelectedUserActivate() {
      this.isAccountActivationModalShown = true;
    },
    onAccountActivationConfirmation() {
      const apiData = { email: this.selectedUser.email };
      adminActivateUser(apiData).then((response) => {
        this.$notify.toast(response["message"]);
        this.getUsersApi();
        this.processUserData();
      });
      this.isAccountActivationModalShown = false;
      this.isEditItemModalShown = false;
    },
    toggleSelectedUserIsBlocked() {
      if (!this.selectedUser.isBlocked) {
        this.isAccountUnblockModalShown = true;
      } else {
        this.isAccountBlockModalShown = true;
      }
    },
    onAccountBlockConfirmation() {
      const apiData = { email: this.selectedUser.email };
      adminBlockUser(apiData).then((response) => {
        this.$notify.toast(response["message"]);
        this.getUsersApi();
        this.processUserData();
        this.isAccountBlockModalShown = false;
        this.isEditItemModalShown = false;
      }).catch(() => {
        this.onAccountBlockCancelation();
      });
    },
    onAccountBlockCancelation() {
      this.selectedUser.isBlocked = (this.selectedUser.isBlocked)? false : true;
      this.isAccountBlockModalShown = false;
    },
    onAccountUnblockConfirmation() {
      const apiData = { email: this.selectedUser.email };
      adminUnblockUser(apiData).then((response) => {
        this.$notify.toast(response["message"]);
        this.getUsersApi();
        this.processUserData();
        this.isAccountUnblockModalShown = false;
        this.isEditItemModalShown = false;
      }).catch(() => {
        this.onAccountUnblockCancelation();
      });
    },
    onAccountUnblockCancelation() {
      this.selectedUser.isBlocked = (this.selectedUser.isBlocked)? false : true;
      this.isAccountUnblockModalShown = false;
    },
    onClickSelectedUserResetPassword() {
      this.isResetPasswordModalShown = true;
    },
    onResetPasswordConfirmation() {
      const apiData = { email: this.selectedUser.email };
      adminResetUserPassword(apiData).then((response) => {
        this.$notify.toast(response["message"]);
        this.getUsersApi();
        this.processUserData();
      });
      this.isResetPasswordModalShown = false;
      this.isEditItemModalShown = false;
    },
    processUserData() {
      this.users = this.users.map((user, index) => {
        return {
          ...user,
          ...{
            index
          }
        };
      });
    },
    getIsActivatedStatus(itemStatus) {
      let item = {};
      switch (itemStatus) {
        case true:
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
        case false:
          item = { color: "#ffffff", text: "Unblocked", textColor: "#000000" };
          break;
        default:
          item = { color: "#ffb3b3", text: "Blocked", textColor: "#ff5252" };
          break;
      }
      return item;
    },
    getUsersApi() {
      adminListUsers()
        .then((response) => {
          this.users.length = 0;
          const rawUsers = response["users"];
          const rawUserIds = Object.keys(rawUsers);
          rawUserIds.forEach(rawUserid => {
            let rawUser = {
              id: rawUserid,
              email: rawUsers[rawUserid]["user_email"],
              isActivated: rawUsers[rawUserid]["user_activated"],
              isBlocked: rawUsers[rawUserid]["user_blocked"]
            };
            this.users.push(rawUser);
          });
        });
    }
  }
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

.edit-modal {
  &__title {
    font-weight: bold;
    margin-bottom: 50 !important;
  }

  &__action-title {
    font-weight: bold;
    margin-bottom: 0 !important;
  }

  &__action-description {
    font-size: smaller;
    padding-bottom: 0 !important;
  }

  &__close-button {
    letter-spacing: 0;
    font-weight: 400;
    text-transform: none;
    text-decoration: none;
  }
}
</style>
