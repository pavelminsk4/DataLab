<template>
  <MainLayout v-if="currentUser" :isTwoColumns="true" style>
    <template #default>
      <MainLayoutTitleBlock
        title="Users"
        description="Manage define limits for users"
        :back-page="{
          name: 'main page',
          routName: 'OnlineHome',
        }"
      >
        <div class="number-users">{{ companyUsers.length }} users</div>
      </MainLayoutTitleBlock>

      <div class="search-wrapper">
        <BaseInput
          v-model="search"
          placeholder="Search users..."
          :isSearch="true"
          class="search-users"
        />

        <BaseButtonWithTooltip
          :is-disabled="isUserCreationAvailable"
          :has-tooltip="isUserCreationAvailable"
          tooltip-title="Created the maximum possible number of users!"
          @click="addNewUser"
        >
          Add User
        </BaseButtonWithTooltip>
      </div>

      <section class="users-section scroll">
        <div
          v-for="(item, index) in filteredUsers"
          :key="'user' + index"
          :class="['user-row', isActiveUser(item) && 'active-user']"
        >
          <UserAvatar
            :avatar-url="item.user_profile.photo"
            :first-name="item.first_name"
            :last-name="item.last_name"
            :username="item.username"
            style="--avatar-width: 32px"
          />

          <div class="name-wrapper">
            <div class="user-name">
              <span>{{ item.first_name + ' ' + item.last_name }}</span>
              <SettingsIcon
                class="icon-button"
                @click="openExistingUserCard(item)"
              />
              <DeleteIcon
                class="icon-button"
                @click="toggleDeleteModal(item)"
              />
            </div>
            <div>{{ item.user_profile.jobtitle }}</div>
          </div>

          <div class="role">
            <BaseDropdown
              :title="currentRole(item.user_profile.role)"
              :name="'name' + index"
            >
              <div
                v-for="role in userRoles"
                :key="role.value"
                @click="updateUserRole(role.value, item.email)"
                class="user-role"
              >
                {{ role.name }}
              </div>
            </BaseDropdown>
          </div>
        </div>
      </section>
    </template>

    <template #second-column>
      <div class="user-options scroll">
        <AreYouSureModal
          v-if="isOpenDeleteModal"
          :item-to-delete="userValue"
          @close="toggleDeleteModal"
          @delete="deleteUserFromCompany"
        />

        <div class="success-message">{{ successMessage }}</div>

        <section v-if="isExistingUser || isNewUser" class="user-data">
          <section v-if="isNewUser">
            <h4 class="group-label">Personal info</h4>
            <div class="label">Email</div>
            <BaseInput
              v-model="email"
              :hasError="!!errors.email"
              :errorMessage="errors.email"
              class="input-field"
            />
            <div class="label">First name</div>
            <BaseInput v-model="firstName" class="input-field" />
            <div class="label">Last name</div>
            <BaseInput v-model="lastName" class="input-field" />

            <h4 class="group-label">Profile settings</h4>
            <div class="label">Username</div>
            <BaseInput
              v-model="username"
              :hasError="!!errors.username"
              :errorMessage="errors.username"
              class="input-field"
            />
            <div class="label">Password</div>
            <BaseInput
              v-model="password"
              :hasError="!!errors.password"
              :errorMessage="errors.password"
              autocomplete="new-password"
              input-type="password"
              class="input-field"
            />
            <div class="label">Confirm password</div>
            <BaseInput
              v-model="confirmPassword"
              :hasError="!!errors.password2"
              :errorMessage="errors.password2"
              autocomplete="new-password"
              input-type="password"
              class="input-field"
            />

            <div class="action-button">
              <BaseButton @click="createNewUser">
                <AddUserIcon />
                <span>Add User</span>
              </BaseButton>
            </div>
          </section>

          <section v-if="isExistingUser">
            <div class="header-existing-user">
              <UserAvatar
                :avatar-url="existingUserData.user_profile.photo"
                :first-name="existingUserData.first_name"
                :last-name="existingUserData.last_name"
                :username="existingUserData.username"
                style="--avatar-width: 72px"
              />

              <div class="name-wrapper">
                <div class="settings-user-name">
                  {{
                    `${existingUserData.first_name} ${existingUserData.last_name}`
                  }}
                </div>
                <div>{{ existingUserData.user_profile.jobtitle }}</div>
              </div>

              <BaseButton
                :is-not-background="true"
                class="delete-button"
                @click="toggleDeleteModal"
              >
                <DeleteIcon />
                <span>Delete User</span>
              </BaseButton>
            </div>

            <div class="label">Name</div>
            <BaseInput v-model="existingUserNameProxy" class="input-field" />
            <div class="label">Surname</div>
            <BaseInput v-model="existingUserSurnameProxy" class="input-field" />
            <div class="label">E-mail</div>
            <BaseInput v-model="existingUserEmailProxy" class="input-field" />

            <div class="action-button">
              <BaseButton @click="updateUserData">
                <UpdateIcon />
                <span>Update User</span>
              </BaseButton>
            </div>
          </section>
        </section>

        <img v-else src="@/assets/users.png" alt="users" />
      </div>
    </template>
  </MainLayout>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'
import {isAllEmptyFields} from '@lib/utilities'

import AddUserIcon from '@/components/icons/AddUserIcon'
import AreYouSureModal from '@/components/modals/AreYouSureModal'
import BaseButton from '@/components/common/BaseButton'
import BaseButtonWithTooltip from '@/components/BaseButtonWithTooltip'
import BaseDropdown from '@/components/BaseDropdown'
import BaseInput from '@/components/common/BaseInput'
import DeleteIcon from '@/components/icons/DeleteIcon'
import MainLayoutTitleBlock from '@/components/layout/MainLayoutTitleBlock'
import MainLayout from '@/components/layout/MainLayout'
import SettingsIcon from '@/components/icons/SettingsIcon'
import UpdateIcon from '@/components/icons/UpdateIcon'
import UserAvatar from '@components/UserAvatar'

export default {
  name: 'UserRolesScreen',
  components: {
    AddUserIcon,
    AreYouSureModal,
    BaseButton,
    BaseButtonWithTooltip,
    BaseDropdown,
    BaseInput,
    DeleteIcon,
    MainLayout,
    MainLayoutTitleBlock,
    SettingsIcon,
    UpdateIcon,
    UserAvatar,
  },
  data() {
    return {
      isNewUser: false,
      isExistingUser: false,
      isOpenDeleteModal: false,
      generalSettingsName: 'General',
      settingsName: ['General', 'Projects'],
      newUsername: '',
      newPassword: '',
      newConfirmPassword: '',
      newEmail: '',
      firstName: '',
      lastName: '',
      successMessage: '',
      existingUserData: null,
      existingUserName: '',
      existingUserSurname: '',
      existingUserEmail: '',
      errors: {
        username: null,
        password: null,
        password2: null,
        email: null,
      },
      search: '',
    }
  },
  computed: {
    ...mapGetters({
      currentUser: get.USER_INFO,
      companyUsers: get.COMPANY_USERS,
      department: get.DEPARTMENT,
    }),
    filteredUsers() {
      if (!this.search) return this.companyUsers

      return this.companyUsers.filter((user) => {
        const fullName = `${user.first_name} ${user.last_name}`.toLowerCase()
        return fullName.includes(this.search.toLowerCase())
      })
    },
    username: {
      get() {
        return this.newUsername
      },
      set(val) {
        this.newUsername = val
        this.errors.username = null
      },
    },
    password: {
      get() {
        return this.newPassword
      },
      set(val) {
        this.newPassword = val
        this.errors.password = null
      },
    },
    confirmPassword: {
      get() {
        return this.newConfirmPassword
      },
      set(val) {
        this.newConfirmPassword = val
        this.errors.password2 = null
      },
    },
    email: {
      get() {
        return this.newEmail
      },
      set(val) {
        this.newEmail = val
        this.errors.email = null
      },
    },
    isUserCreationAvailable() {
      return (
        this.department.current_number_of_users >= this.department.max_users
      )
    },
    existingUserNameProxy: {
      get() {
        return this.existingUserData.first_name || this.existingUserName
      },
      set(value) {
        this.existingUserName = value
      },
    },
    existingUserSurnameProxy: {
      get() {
        return this.existingUserData.last_name || this.existingUserSurname
      },
      set(value) {
        this.existingUserSurname = value
      },
    },
    existingUserEmailProxy: {
      get() {
        return this.existingUserData.email || this.existingUserEmail
      },
      set(value) {
        this.existingUserEmail = value
      },
    },
    userValue() {
      return {
        type: 'user',
        name:
          this.existingUserData.first_name +
          ' ' +
          this.existingUserData.last_name,
      }
    },
  },
  async created() {
    this.userRoles = [
      {name: 'Company', value: 'company'},
      {name: 'Regular User', value: 'regular_user'},
      {name: 'Picker', value: 'picker'},
      {name: 'Writer', value: 'writer'},
      {name: 'Publisher', value: 'publisher'},
    ]

    if (!this.currentUser) {
      await this[action.GET_USER_INFORMATION]()
    }

    await this[action.GET_COMPANY_USERS](
      this.currentUser?.user_profile?.department.id
    )
  },
  methods: {
    ...mapActions([
      action.GET_COMPANY_USERS,
      action.GET_USER_INFORMATION,
      action.CREATE_NEW_USER,
      action.PUT_USER_DEPARTMENT,
      action.UPDATE_USER_DATA,
      action.DELETE_USER_FROM_COMPANY,
    ]),
    addNewUser() {
      this.successMessage = ''
      this.isExistingUser = false
      this.isNewUser = true
    },
    async createNewUser() {
      if (!this.validation()) return

      const response = await this[action.CREATE_NEW_USER]({
        username: this.username,
        password: this.password,
        password2: this.confirmPassword,
        email: this.email,
        first_name: this.firstName,
        last_name: this.lastName,
      })

      if (response?.hasError) {
        Object.keys(response).forEach((key) => {
          this.errors[key] = response[key][0]
        })
      }

      if (!isAllEmptyFields(this.errors)) return

      await this[action.PUT_USER_DEPARTMENT]({
        email: this.email,
        data: {
          department: this.currentUser?.user_profile?.department.id,
        },
        userId: this.currentUser?.user_profile?.department.id,
      })

      this.isNewUser = false
      this.successMessage = 'User created!'
    },
    updateUserRole(value, email) {
      this[action.PUT_USER_DEPARTMENT]({
        email: email,
        data: {
          role: value,
        },
        userId: this.currentUser?.user_profile?.department.id,
      })
    },
    currentRole(value) {
      return this.userRoles.find((el) => el.value === value)?.name
    },
    openExistingUserCard(existingUserData) {
      this.successMessage = ''
      this.existingUserData = existingUserData
      this.isNewUser = false
      this.isExistingUser = true
    },
    async updateUserData() {
      await this[action.UPDATE_USER_DATA]({
        userId: this.existingUserData.id,
        data: {
          first_name: this.existingUserName,
          last_name: this.existingUserSurname,
          email: this.existingUserEmail,
        },
        currentUserId: this.currentUser?.user_profile?.department.id,
      })
    },
    async deleteUserFromCompany() {
      await this[action.DELETE_USER_FROM_COMPANY]({
        userId: this.existingUserData.id,
        currentUserId: this.currentUser?.user_profile?.department.id,
      })

      this.isExistingUser = false

      await this.toggleDeleteModal()
    },
    toggleDeleteModal(user) {
      if (user) {
        this.existingUserData = user
      }

      this.isOpenDeleteModal = !this.isOpenDeleteModal
      this.togglePageScroll(this.isOpenDeleteModal)
    },
    validation() {
      const defaultErrorMessage = 'required'

      this.errors.username = this.username ? null : defaultErrorMessage
      this.errors.password = this.password ? null : defaultErrorMessage
      if (this.confirmPassword) {
        this.errors.password2 =
          this.password === this.confirmPassword
            ? null
            : `passwords don't match`
      } else {
        this.errors.password2 = defaultErrorMessage
      }
      this.errors.email = this.email ? null : defaultErrorMessage

      return isAllEmptyFields(this.errors)
    },
    isActiveUser(user) {
      return this.isExistingUser && this.existingUserData.id === user.id
    },
  },
}
</script>

<style lang="scss" scoped>
.number-users {
  align-self: flex-end;

  font-weight: 600;
  line-height: 20px;
  color: var(--typography-secondary-color);
}

.search-wrapper {
  display: flex;
  gap: 16px;

  margin-bottom: 24px;
}

.search-users {
  flex-grow: 1;
}

.users-section {
  width: 100%;
  height: calc(100% - 200px);
  padding-right: 24px;

  .user-row {
    display: flex;

    padding: 8px 12px;

    border-radius: var(--border-radius);
    border: 1px solid transparent;

    &:hover {
      background-color: var(--primary-active-color);
    }

    .name-wrapper {
      flex-grow: 1;
      display: flex;
      flex-direction: column;
    }

    .user-name {
      display: flex;
      gap: 14px;
      font-weight: 600;
    }

    .settings-user-name {
      font-weight: 500;
      font-size: 18px;
    }
  }

  .active-user {
    background-color: var(--primary-active-color);
    border: 1px solid var(--border-active-color);
  }
}

.user-role {
  white-space: nowrap;

  padding: 10px;

  &:hover {
    background-color: var(--button-primary-color);
  }

  &:first-child {
    border-radius: 10px 10px 0 0;
  }

  &:last-child {
    border-radius: 0 0 10px 10px;
  }
}

.user-options {
  display: flex;
  justify-content: center;
  align-items: center;

  width: 63vw;
  height: 100%;
}

.user-data {
  display: flex;
  flex-direction: column;

  width: 45%;
  padding: 24px;

  @media (max-width: 1440px) {
    width: 408px;
  }

  @media (max-width: 900px) {
    width: 100%;
  }

  .group-label {
    margin-bottom: 20px;

    font-weight: 500;
    font-size: 16px;
  }

  .label {
    color: var(--typography-title-color);
  }

  .input-field {
    margin: 10px 0 25px;
  }
}

.action-button {
  display: flex;
  justify-content: flex-end;

  width: 100%;
}

.user-card-name {
  display: flex;

  .name {
    display: flex;
    align-items: center;
    gap: 15px;
  }
}

.header-existing-user {
  display: flex;
  align-items: center;

  margin-bottom: 21px;

  color: var(--typography-primary-color);

  .delete-button {
    border: none;
  }
}

.success-message {
  color: var(--typography-primary-color);
}
</style>
