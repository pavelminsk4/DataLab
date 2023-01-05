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
            class="user"
          >
            <img :src="item.user_profile.photo" class="photo" />
            <div class="name-wrapper">
              <div>{{ item.first_name + ' ' + item.last_name }}</div>
              <div class="hint">{{ item.user_profile.jobtitle }}</div>
            </div>
            <div class="role">{{ item.user_profile.role }}</div>
          </div>
        </div>
      </section>

      <div class="success-message">{{ successMessage }}</div>

      <section v-if="isNewUser" class="user-data">
        <section v-if="isNewUser">
          <div class="title">Username</div>
          <BaseInput v-model="username" class="input" />
          <div class="title">Password</div>
          <BaseInput v-model="password" type="password" class="input" />
          <div class="title">Confirm password</div>
          <BaseInput v-model="confirmPassword" type="password" class="input" />
          <div class="title">Email</div>
          <BaseInput v-model="email" class="input" />
          <div class="title">First name</div>
          <BaseInput v-model="firstName" class="input" />
          <div class="title">Last name</div>
          <BaseInput v-model="lastName" class="input" />

          <BaseButton @click="createNewUser">Add User</BaseButton>
        </section>
      </section>
    </div>
  </MainLayout>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import MainLayout from '@/components/layout/MainLayout'
import NavigationBar from '@/components/navigation/NavigationBar'
import BaseButton from '@/components/buttons/BaseButton'
import BaseInput from '@/components/BaseInput'

export default {
  name: 'UserRolesScreen',
  components: {BaseInput, BaseButton, NavigationBar, MainLayout},
  data() {
    return {
      isNewUser: false,
      isUserData: false,
      generalSettingsName: 'General',
      settingsName: ['General', 'Projects'],
      username: '',
      password: '',
      confirmPassword: '',
      email: '',
      firstName: '',
      lastName: '',
      successMessage: '',
    }
  },
  async created() {
    await this[action.GET_USER_INFORMATION]()

    await this[action.GET_COMPANY_USERS](
      this.currentUser?.user_profile?.department.id
    )
  },
  computed: {
    ...mapGetters({
      currentUser: get.USER_INFO,
      companyUsers: get.COMPANY_USERS,
    }),
  },
  methods: {
    ...mapActions([
      action.GET_COMPANY_USERS,
      action.GET_USER_INFORMATION,
      action.CREATE_NEW_USER,
    ]),
    addNewUser() {
      this.successMessage = ''
      this.isNewUser = true
    },
    createNewUser() {
      this[action.CREATE_NEW_USER]({
        username: this.username,
        password: this.password,
        password2: this.confirmPassword,
        email: this.email,
        first_name: this.firstName,
        last_name: this.lastName,
      })

      this.isNewUser = false
      this.successMessage = 'User created!'
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
  gap: 85px;

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

    .input {
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

    .delete-button {
      display: flex;
      align-items: center;
      gap: 6px;

      margin-left: auto;

      font-style: normal;
      font-weight: 400;
      font-size: 14px;
      line-height: 22px;
      color: var(--primary-button-color);
    }
  }

  .user-card-header {
    display: flex;
    gap: 25px;

    margin: 20px 0;

    border-bottom: 1px solid var(--border-color);

    cursor: pointer;

    font-style: normal;
    font-weight: 400;
    font-size: 14px;
    line-height: 22px;
    color: rgba(255, 255, 255, 0.8);

    .active-user-card {
      padding-bottom: 10px;

      border-bottom: 2px solid var(--primary-button-color);

      color: var(--primary-text-color);
    }
  }
}

.success-message {
  color: var(--primary-text-color);
}
</style>
