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
    </div>
  </header>
</template>

<script>
import BaseInput from "@/components/BaseInput";
import LogoIcon from '../icons/LogoIcon'
import UserWithoutPhotoIcon from '../icons/UserWithoutPhotoIcon'
import ActiveBellIcon from '../icons/ActiveBellIcon'
import ArrowDownIcon from '../icons/ArrowDownIcon'

export default {
  name: "MainHeader",
  components: {
    LogoIcon,
    BaseInput,
    UserWithoutPhotoIcon,
    ActiveBellIcon,
    ArrowDownIcon
  }
}
</script>

<style scoped>
  .header {
    display: flex;
    justify-content: space-between;

    width: 100%;
    height: 82px;
    padding: 13px 69px 29px 80px;
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
</style>