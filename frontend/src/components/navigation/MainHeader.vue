<template>
  <header class="header">
    <section class="section-search">
      <LogoIcon class="logo" />
      <BaseInput />
    </section>

    <div class="section-company">
      <UserWithoutPhotoIcon class="user-icon" />
      <ActiveBellIcon class="bell-icon" />

      <div class="company-dropdown">
        Company Name
        <ArrowDownIcon class="arrow-down" />
      </div>
      <div class="company-logo">
        Logo
      </div>
      <BaseButton @click="logout" class="logout">Logout</BaseButton>
    </div>
  </header>
</template>

<script>
import { mapActions } from 'vuex'
import { action } from '@store/constants'

import BaseInput from '@components/BaseInput'
import BaseButton from '@components/buttons/BaseButton'

import LogoIcon from '@components/icons/LogoIcon'
import ArrowDownIcon from '@components/icons/ArrowDownIcon'
import ActiveBellIcon from '@components/icons/ActiveBellIcon'
import UserWithoutPhotoIcon from '@components/icons/UserWithoutPhotoIcon'

export default {
  name: "MainHeader",
  components: {
    BaseButton,
    LogoIcon,
    BaseInput,
    UserWithoutPhotoIcon,
    ActiveBellIcon,
    ArrowDownIcon
  },
  methods: {
    ...mapActions([action.LOGOUT]),

    async logout() {
      await this[action.LOGOUT]()
    }
  }
}
</script>

<style scoped>
  .header {
    box-sizing: border-box;

    display: flex;
    justify-content: space-between;

    height: 82px;
    padding: 13px 0 29px 0;
  }

  .logo {
    width: 75px;
    height: 30px;
    margin: 5px 65px 0 0;
  }

  .section-search {
    display: flex;
  }

  .section-company {
    display: flex;
  }

  .user-icon {
    margin: 10px 43px 0 0;
  }

  .bell-icon {
    margin: 10px 55px 0 0;
  }

  .company-dropdown {
    height: fit-content;
    margin: 12px 11px 0 0;

    color: var(--primary-text-color);
  }

  .arrow-down {
    margin-left: 6px;
  }

  .company-logo {
    display: flex;
    align-items: center;
    justify-content: center;

    height: 36px;
    width: 36px;
    margin-top: 7px;

    border-radius: 100%;

    color: var(--primary-text-color);
    background-color: var(--primary-button-color);

    font-size: 8px;
  }

  .logout {
    margin: 7px 0 0 10px;
  }
</style>
