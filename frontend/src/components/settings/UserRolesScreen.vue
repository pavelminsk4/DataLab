<template>
  <MainLayout v-if="currentUser">
    <NavigationBar
      title="Users"
      hint="Manage define limits for users"
      :is-back-to-dashboard="true"
    />

    <div class="users-menu">
      <div class="tab-name">Users</div>
    </div>

    <div class="user-roles-wrapper">
      <section class="users-section">
        <div class="users-section-header">
          <div class="title">
            <div>Users</div>
            <div>{{ companyUsers.length }}</div>
          </div>
          <BaseButton @click="addNewUser" class="button"> Add User </BaseButton>
        </div>

        <div class="users-wrapper scroll">
          <div
            v-for="(item, index) in companyUsers"
            :key="'user' + index"
            @click="openExistingUserCard(item)"
            class="user"
          >
            <img :src="item.user_profile.photo" class="photo" />
            <div class="name-wrapper">
              <div>{{ item.first_name + ' ' + item.last_name }}</div>
              <div class="hint">{{ item.user_profile.jobtitle }}</div>
            </div>
            <div class="role">
              <BaseDropdown
                :title="currentRole(item.user_profile.role)"
                :id="index"
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
        </div>
      </section>

      <div class="success-message">{{ successMessage }}</div>

      <section v-if="isExistingUser || isNewUser" class="user-data">
        <section v-if="isNewUser">
          <div class="title">Username</div>
          <BaseInput
            v-model="username"
            :hasError="!!errors.username"
            :errorMessage="errors.username"
            class="input-field"
          />
          <div class="title">Password</div>
          <BaseInput
            v-model="password"
            :hasError="!!errors.password"
            :errorMessage="errors.password"
            autocomplete="new-password"
            input-type="password"
            class="input-field"
          />
          <div class="title">Confirm password</div>
          <BaseInput
            v-model="confirmPassword"
            :hasError="!!errors.password2"
            :errorMessage="errors.password2"
            autocomplete="new-password"
            input-type="password"
            class="input-field"
          />
          <div class="title">Email</div>
          <BaseInput
            v-model="email"
            :hasError="!!errors.email"
            :errorMessage="errors.email"
            class="input-field"
          />
          <div class="title">First name</div>
          <BaseInput v-model="firstName" class="input-field" />
          <div class="title">Last name</div>
          <BaseInput v-model="lastName" class="input-field" />

          <BaseButton @click="createNewUser">Add User</BaseButton>
        </section>

        <section v-if="isExistingUser">
          <div class="header-existing-user">
            <img :src="existingUserData.user_profile.photo" class="photo" />
            <div>
              <div>{{ existingUserData.first_name }}</div>
              <div>{{ existingUserData.last_name }}</div>
            </div>

            <div @click="toggleDeleteModal" class="delete-button">
              <PlusIcon class="icon-delete" />Delete User
            </div>

            <AreYouSureModal
              v-if="isOpenDeleteModal"
              :item-to-delete="userValue"
              @close="toggleDeleteModal"
              @delete="deleteUserFromCompany"
            />
          </div>

          <div class="title">Name</div>
          <BaseInput v-model="existingUserNameProxy" class="input-field" />
          <div class="title">Surname</div>
          <BaseInput v-model="existingUserSurnameProxy" class="input-field" />
          <div class="title">E-mail</div>
          <BaseInput v-model="existingUserEmailProxy" class="input-field" />

          <BaseButton @click="updateUserData">Update User</BaseButton>
        </section>
      </section>
    </div>
  </MainLayout>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'
import {isAllEmptyFields} from '@lib/utilities'

import MainLayout from '@/components/layout/MainLayout'
import NavigationBar from '@/components/navigation/NavigationBar'
import BaseButton from '@/components/buttons/BaseButton'
import BaseInput from '@/components/BaseInput'
import BaseDropdown from '@/components/BaseDropdown'
import PlusIcon from '@/components/icons/PlusIcon'
import AreYouSureModal from '@/components/modals/AreYouSureModal'

export default {
  name: 'UserRolesScreen',
  components: {
    AreYouSureModal,
    PlusIcon,
    BaseDropdown,
    BaseInput,
    BaseButton,
    NavigationBar,
    MainLayout,
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
    }
  },
  computed: {
    ...mapGetters({
      currentUser: get.USER_INFO,
      companyUsers: get.COMPANY_USERS,
    }),
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

      Object.keys(response).forEach((key) => {
        this.errors[key] = response[key][0]
      })

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
    toggleDeleteModal() {
      this.isOpenDeleteModal = !this.isOpenDeleteModal
      this.togglePageScroll(this.isOpenDeleteModal)
    },
    validation() {
      const defaultErrorMessage = 'required'

      this.errors.username = this.username ? null : defaultErrorMessage
      this.errors.password = this.password ? null : defaultErrorMessage
      if (this.confirmPassword) {
        console.log(this.password === this.confirmPassword)
        this.errors.password2 =
          this.password === this.confirmPassword
            ? null
            : `passwords don't match`

        console.log(this.errors.password2)
      } else {
        this.errors.password2 = defaultErrorMessage
      }
      this.errors.email = this.email ? null : defaultErrorMessage

      return isAllEmptyFields(this.errors)
    },
  },
}
</script>

<style lang="scss" scoped>
.users-menu {
  margin: 40px 0;

  border-bottom: 1px solid var(--border-color);

  cursor: pointer;

  font-style: normal;
  font-weight: 500;
  font-size: 14px;
  line-height: 22px;
  color: var(--primary-text-color);

  .tab-name {
    width: fit-content;
    padding-bottom: 10px;

    border-bottom: 2px solid var(--primary-button-color);
  }
}
.user-roles-wrapper {
  display: flex;
  gap: 30px;

  .users-section {
    width: 50%;
    height: 580px;
    padding: 20px;

    background: var(--secondary-bg-color);
    border: 1px solid var(--border-color);
    box-shadow: 0 4px 10px rgba(16, 16, 16, 0.25);
    border-radius: 10px;

    .users-section-header {
      display: flex;
      justify-content: space-between;

      margin-bottom: 42px;

      .title {
        display: flex;
        gap: 14px;

        font-style: normal;
        font-weight: 600;
        font-size: 16px;
        line-height: 22px;
        color: var(--primary-text-color);
      }

      .button {
        width: 120px;
      }
    }

    .user {
      display: flex;

      margin-bottom: 15px;

      cursor: pointer;

      .photo {
        width: 36px;
        height: 36px;
        margin-right: 16px;

        border-radius: 100px;
      }

      .name-wrapper {
        display: flex;
        flex-direction: column;

        font-style: normal;
        font-weight: 500;
        font-size: 14px;
        line-height: 110%;
        color: var(--primary-text-color);

        .hint {
          font-style: normal;
          font-weight: 500;
          font-size: 12px;
          line-height: 16px;
          color: var(--secondary-text-color);
        }
      }

      .role {
        margin-left: auto;

        font-size: 14px;
        color: var(--primary-text-color);
      }
    }
  }

  .users-wrapper {
    height: 450px;
    padding-right: 15px;

    overflow: auto;
  }

  .user-data {
    height: fit-content;
    width: 50%;
    padding: 40px;

    background: var(--secondary-bg-color);
    border: 1px solid var(--border-color);
    box-shadow: 0 4px 10px rgba(16, 16, 16, 0.25);
    border-radius: 10px;

    .title {
      font-style: normal;
      font-weight: 500;
      font-size: 14px;
      line-height: 110%;
      color: var(--primary-text-color);
    }

    .input-field {
      width: 100%;
      margin: 10px 0 25px 0;
    }
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

    color: var(--primary-text-color);

    .photo {
      width: 66px;
      height: 66px;
      margin-right: 15px;

      border-radius: 100px;
    }

    .delete-button {
      display: flex;
      align-items: center;
      gap: 6px;

      margin-left: auto;

      cursor: pointer;

      font-style: normal;
      font-weight: 400;
      font-size: 14px;
      line-height: 22px;
      color: var(--primary-button-color);

      .icon-delete {
        transform: rotate(45deg);
      }

      &:hover {
        color: var(--secondary-text-color);
      }
    }
  }
}

.user-role {
  white-space: nowrap;

  padding: 10px;

  &:hover {
    background-color: var(--primary-button-color);
  }

  &:first-child {
    border-radius: 10px 10px 0 0;
  }

  &:last-child {
    border-radius: 0 0 10px 10px;
  }
}

.success-message {
  color: var(--primary-text-color);
}
</style>
