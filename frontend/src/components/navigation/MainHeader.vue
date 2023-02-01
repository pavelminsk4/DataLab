<template>
  <header :class="['header', !isVisibleLogo && 'is-not-visible-logo']">
    <LogoIcon v-if="isVisibleLogo" class="logo" @click="goToDashboard" />

    <div class="header-navigation">
      <div
        v-if="userInfo?.user_profile?.role === 'company'"
        @click="goToUserRolesPage"
        :class="['header-tab', isActiveTab && 'active-tab']"
      >
        <UserIcon /> Users
      </div>

      <div class="section-company">
        <div class="name">{{ companyName }}</div>
        <section class="dropdown-wrapper">
          <ArrowDownIcon
            @click="openDropdown"
            :class="[isOpenDropdown && 'arrow-open-dropdown', 'arrow-down']"
          />

          <div v-if="isOpenDropdown" class="dropdown">
            <div @click="logout" class="item">Logout</div>
          </div>
        </section>
        <img :src="logoImg" class="company-logo" />
      </div>
    </div>
  </header>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import LogoIcon from '@components/icons/LogoIcon'
import ArrowDownIcon from '@components/icons/ArrowDownIcon'
import UserIcon from '@/components/icons/UserIcon'

export default {
  name: 'MainHeader',
  components: {
    UserIcon,
    LogoIcon,
    ArrowDownIcon,
  },
  props: {
    isVisibleLogo: {
      type: Boolean,
      default: true,
    },
  },
  data() {
    return {
      isOpenDropdown: false,
    }
  },
  created() {
    document.addEventListener('click', this.closeDropdown)
  },
  computed: {
    ...mapGetters({userInfo: get.USER_INFO}),
    companyName() {
      return this.userInfo?.username
    },
    logoImg() {
      return this.userInfo?.user_profile?.photo
    },
    isActiveTab() {
      return this.$route.name === 'UserRoles'
    },
  },
  methods: {
    ...mapActions([action.LOGOUT]),
    logout() {
      this[action.LOGOUT]()
    },

    goToDashboard() {
      this.$router.push({
        name: 'Home',
      })
    },
    goToUserRolesPage() {
      this.$router.push({
        name: 'UserRoles',
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

.header-navigation {
  display: flex;
  align-items: center;
}

.header-tab {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 6px;

  height: 38px;
  width: 90px;
  margin-right: 35px;

  cursor: pointer;

  font-style: normal;
  font-weight: 400;
  font-size: 14px;
  line-height: 150%;

  color: var(--primary-text-color);

  &:hover {
    border-radius: 10px;
    background: rgba(5, 95, 252, 0.6);
  }
}

.is-not-visible-logo {
  justify-content: end;
}

.logo {
  cursor: pointer;
  opacity: 0;

  width: 0;
  height: 0;
}

.section-company {
  display: flex;
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

  cursor: pointer;

  font-size: 12px;

  .dropdown {
    z-index: 1000;

    position: absolute;
    top: 40px;
    right: 2px;

    display: flex;
    flex-direction: column;

    cursor: pointer;

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
    }

    &:hover {
      background-color: var(--button-primary-color);
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
    color: var(--button-primary-color);
  }
}

.arrow-open-dropdown {
  transform: rotate(180deg);
  color: var(--button-primary-color);
}

.company-logo {
  display: flex;
  align-items: center;
  justify-content: center;

  height: 36px;
  width: 36px;

  border-radius: 100%;

  color: var(--primary-text-color);
  background-color: var(--button-primary-color);

  font-size: 8px;
}

.logout {
  margin: 7px 0 0 10px;
}

.active-tab {
  display: flex;
  align-items: center;
  justify-content: center;

  height: 38px;
  width: 90px;

  border-radius: 10px;
  background-color: var(--button-primary-color);
}
</style>
