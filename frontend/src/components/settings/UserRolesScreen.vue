<template>
  <MainLayout>
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
            <div>Count</div>
          </div>
          <BaseButton @click="addNewUser" class="button"> Add User </BaseButton>
        </div>

        <div @click="updateUserData" class="user">
          <div class="photo">PHOTO</div>
          <div class="name-wrapper">
            <div>NAME</div>
            <div class="hint">ROLE</div>
          </div>
          <div class="role">Admin</div>
        </div>
      </section>

      <section v-if="isNewUser || isUserData" class="user-data">
        <section v-if="isNewUser">
          <div class="title">Name</div>
          <BaseInput class="input" />
          <div class="title">E-mail</div>
          <BaseInput class="input" />

          <BaseButton>Add User</BaseButton>
        </section>

        <section v-if="isUserData">
          <div class="user-card-name">
            <div class="name">
              <div>PHOTO</div>
              <div>NAME</div>
            </div>

            <div class="delete-button"><CrossIcon /> Delete User</div>
          </div>

          <div class="user-card-header">
            <div
              v-for="button in settingsName"
              :key="button"
              :class="[generalSettingsName === button && 'active-user-card']"
              @click="toggleSettings"
            >
              {{ button }}
            </div>
          </div>

          <div class="title">Name</div>
          <BaseInput class="input" />
          <div class="title">Surname</div>
          <BaseInput class="input" />
          <div class="title">E-mail</div>
          <BaseInput class="input" />

          <BaseButton>Update</BaseButton>
        </section>
      </section>
    </div>
  </MainLayout>
</template>

<script>
import MainLayout from '@/components/layout/MainLayout'
import NavigationBar from '@/components/navigation/NavigationBar'
import BaseButton from '@/components/buttons/BaseButton'
import BaseInput from '@/components/BaseInput'
import CrossIcon from '@/components/icons/CrossIcon'
export default {
  name: 'UserRolesScreen',
  components: {CrossIcon, BaseInput, BaseButton, NavigationBar, MainLayout},
  data() {
    return {
      isNewUser: false,
      isUserData: false,
      generalSettingsName: 'General',
      settingsName: ['General', 'Projects'],
    }
  },
  methods: {
    addNewUser() {
      this.isNewUser = true
    },
    updateUserData() {
      this.isUserData = true
    },
    toggleSettings(e) {
      this.generalSettingsName = e.target.innerText
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

      cursor: pointer;

      .photo {
        margin-right: 16px;
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

        color: var(--primary-text-color);
      }
    }
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
</style>
