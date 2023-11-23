<template>
  <header class="header">
    <div class="header-logo">
      <LogoIcon
        class="logo"
        @click="goToMainPage"
        @click.middle="goToMainPageNewTab"
      />
    </div>

    <div class="header-navigation">
      <div
        v-if="userInfo?.user_profile?.role === 'company'"
        @click="goToUserRolesPage"
        :class="['header-tab', isActiveTab && 'active-tab']"
      >
        <UserIcon :class="['icon', isActiveTab && 'active-icon']" />
        <CustomText tag="span" text="Users" />
      </div>

      <div class="section-company">
        <div class="name">{{ companyName }}</div>
        <UserAvatar
          v-if="userInfo"
          :avatar-url="logoImg"
          :first-name="userInfo?.first_name"
          :last-name="userInfo?.last_name"
          :username="userInfo.username"
          style="--avatar-width: 32px"
        />
        <section class="dropdown-wrapper">
          <ArrowDownIcon
            @click="toogleDropdown"
            :class="[isOpenDropdown && 'arrow-open-dropdown', 'arrow-down']"
          />

          <div v-if="isOpenDropdown" class="dropdown-menu">
            <ProfileMenu
              :user-info="userInfo"
              @logout="logout"
              @close-pop-up="toogleDropdown"
            />
          </div>
        </section>
      </div>
    </div>
  </header>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'
import {capitalizeFirstLetter} from '@lib/utilities'

import CustomText from '@components/CustomText'
import UserAvatar from '@components/UserAvatar'
import LogoIcon from '@components/icons/LogoIcon'
import ArrowDownIcon from '@components/icons/ArrowDownIcon'
import UserIcon from '@components/icons/UserIcon'
import ProfileMenu from '@components/navigation/ProfileMenu'

export default {
  name: 'MainHeader',
  components: {
    UserIcon,
    LogoIcon,
    ArrowDownIcon,
    UserAvatar,
    CustomText,
    ProfileMenu,
  },
  data() {
    return {
      isOpenDropdown: false,
    }
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
  created() {
    document.addEventListener('click', this.closeDropdown)
  },
  unmounted() {
    document.removeEventListener('click', this.closeDropdown)
  },
  methods: {
    capitalizeFirstLetter,
    ...mapActions([action.LOGOUT]),
    logout() {
      this[action.LOGOUT]()
    },

    goToMainPage() {
      this.$router.push({
        name: 'MainView',
      })
    },
    goToMainPageNewTab() {
      let route = this.$router.resolve({name: 'MainView'})
      window.open(route.href)
    },
    goToUserRolesPage() {
      this.$router.push({
        name: 'UserRoles',
      })
    },
    toogleDropdown() {
      this.isOpenDropdown = !this.isOpenDropdown
    },
    closeDropdown({target}) {
      const selectList = document.querySelector('.dropdown-wrapper')

      if (!selectList?.contains(target)) {
        this.isOpenDropdown = false
      }
    },
  },
}
</script>

<style lang="scss" scoped>
.header {
  position: absolute;
  top: 0;
  left: 0;
  z-index: 2;

  display: flex;
  align-items: center;
  justify-content: space-between;

  width: 100%;
  height: var(--header-height);

  background-color: var(--background-secondary-color);
  border: var(--border-primary);
}

.header-logo {
  display: flex;
  gap: 25px;
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
  line-height: 20px;

  &:hover {
    border-radius: 10px;
    background: rgba(5, 95, 252, 0.6);
    color: var(--button-text-color);
  }
}

.logo {
  margin-left: 32px;

  cursor: pointer;
}

.section-company {
  display: flex;
}

.name {
  display: flex;
  align-items: center;

  margin-right: 8px;

  font-style: normal;
  font-weight: 500;
  font-size: 14px;
  line-height: 20px;
}

.dropdown-wrapper {
  position: relative;

  display: flex;
  align-items: center;

  margin-right: 32px;

  cursor: pointer;

  font-size: 12px;

  .dropdown-menu {
    z-index: 1000;

    position: absolute;
    top: 40px;
    right: 2px;

    display: flex;
    flex-direction: column;

    background: var(--background-secondary-color);
    border-radius: 10px;

    font-style: normal;
    font-weight: 400;
    font-size: 12px;
    line-height: 20px;
  }
}

.arrow-down {
  cursor: pointer;

  width: 10px;
  height: 10px;

  margin: 0 11px 0 7px;

  color: var(--typography-secondary-color);

  &:hover {
    color: var(--button-primary-color);
  }
}

.arrow-open-dropdown {
  transform: rotate(180deg);
  color: var(--button-primary-color);
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
  border: 1px solid var(--button-primary-color);

  color: var(--primary-color);

  .active-icon {
    color: var(--primary-color);
  }

  &:hover {
    .active-icon {
      color: var(--button-text-color);
    }

    color: var(--button-text-color);
  }
}
</style>
