<template>
  <header class="header">
    <LogoIcon class="logo" @click="goToDashboard" />

    <div class="section-company">
      <UserWithoutPhotoIcon />
      <ActiveBellIcon class="bell-icon" />
      <div class="name">Company Name</div>
      <section class="dropdown-wrapper">
        <ArrowDownIcon
          @click="openDropdown"
          :class="[isOpenDropdown && 'arrow-open-dropdown', 'arrow-down']"
        />

        <div v-if="isOpenDropdown" class="dropdown">
          <div class="item">Settings</div>
          <div @click="logout" class="item">Logout</div>
        </div>
      </section>
      <div class="company-logo">Logo</div>
    </div>
  </header>
</template>

<script>
import {mapActions} from 'vuex'
import {action} from '@store/constants'

import LogoIcon from '@components/icons/LogoIcon'
import ArrowDownIcon from '@components/icons/ArrowDownIcon'
import ActiveBellIcon from '@components/icons/ActiveBellIcon'
import UserWithoutPhotoIcon from '@components/icons/UserWithoutPhotoIcon'

export default {
  name: 'MainHeader',
  components: {
    LogoIcon,
    UserWithoutPhotoIcon,
    ActiveBellIcon,
    ArrowDownIcon,
  },
  data() {
    return {
      isOpenDropdown: false,
    }
  },
  created() {
    document.addEventListener('click', this.closeDropdown)
  },
  methods: {
    ...mapActions([action.LOGOUT]),

    async logout() {
      await this[action.LOGOUT]()
    },

    goToDashboard() {
      this.$router.push({
        name: 'Home',
      })
    },
    openDropdown() {
      this.isOpenDropdown = !this.isOpenDropdown
    },
    closeDropdown() {
      const elements = document.querySelectorAll('.dropdown-wrapper')

      if (!Array.from(elements).find((el) => el.contains(event.target))) {
        this.isOpenDropdown = false
      }
    },
  },
}
</script>

<style lang="scss" scoped>
.header {
  box-sizing: border-box;

  display: flex;
  align-items: center;
  justify-content: space-between;

  height: 66px;
  margin-bottom: 28px;
}

.logo {
  cursor: pointer;

  width: 75px;
  height: 30px;
}

.section-company {
  display: flex;
}

.bell-icon {
  margin: 0 55px 0 43px;
}

.name {
  display: flex;
  align-items: center;

  font-style: normal;
  font-weight: 500;
  font-size: 14px;
  line-height: 20px;
  color: var(--primary-text-color);
}

.dropdown-wrapper {
  position: relative;

  display: flex;
  align-items: center;

  .dropdown {
    position: absolute;
    top: 40px;
    right: 2px;

    display: flex;
    flex-direction: column;

    background: var(--progress-line);
    border: 1px solid var(--modal-border-color);
    border-radius: 10px;

    font-style: normal;
    font-weight: 400;
    font-size: 12px;
    line-height: 20px;
    color: var(--primary-text-color);

    .item {
      cursor: pointer;

      padding: 9px 24px 8px;

      &:hover {
        color: var(--primary-button-color);
      }

      &:first-child {
        border-bottom: 1px solid var(--modal-line-color);
      }
    }
  }
}

.arrow-down {
  cursor: pointer;

  width: 10px;
  height: 10px;

  margin: 0 11px 0 7px;

  color: var(--primary-text-color);

  &:hover {
    color: var(--primary-button-color);
  }
}

.arrow-open-dropdown {
  transform: rotate(180deg);
  color: var(--primary-button-color);
}

.company-logo {
  display: flex;
  align-items: center;
  justify-content: center;

  height: 36px;
  width: 36px;

  border-radius: 100%;

  color: var(--primary-text-color);
  background-color: var(--primary-button-color);

  font-size: 8px;
}

.logout {
  margin: 7px 0 0 10px;
}
</style>
