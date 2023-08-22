<template>
  <div class="profile-menu-wrapper">
    <div class="user-name">
      <UserAvatar
        v-if="userInfo"
        :avatar-url="logoImg"
        :first-name="userInfo?.first_name"
        :last-name="userInfo?.last_name"
        :username="userInfo.username"
        style="--avatar-width: 72px"
      />
      <div class="name">
        {{ userInfo.first_name + ' ' + userInfo.last_name }}
      </div>
      <div class="email">{{ userInfo.email }}</div>
    </div>

    <div
      v-for="item in settings"
      :key="item.name"
      class="setting"
      @click="$emit(item.action)"
    >
      <component :is="item.icon" />
      {{ item.name }}
    </div>

    <div class="laguages">LANGUAGE</div>

    <div
      v-for="(item, index) in availableLanguages"
      :key="item.lang + index"
      class="lang-item"
      @click="updateLanguage(item.value)"
    >
      <component :is="getIcon(item.value)" />
      {{ item.lang }}
      <ArrowheadIcon
        v-if="item.value === platformLanguage"
        direction="bottom"
        class="arrow-icon"
      />
    </div>
  </div>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'
import {capitalizeFirstLetter} from '@/lib/utilities'

import UserAvatar from '@components/UserAvatar'
import EnIcon from '@components/icons/languages/EnIcon'
import ArIcon from '@components/icons/languages/ArIcon'
import LogoutIcon from '@components/icons/LogoutIcon'
import ArrowheadIcon from '@/components/icons/ArrowheadIcon'

export default {
  name: 'ProfileMenu',
  components: {UserAvatar, ArrowheadIcon, ArIcon, EnIcon, LogoutIcon},
  props: {
    userInfo: {type: Object, requred: true},
  },
  data() {
    return {
      settings: [{name: 'Logout', icon: 'LogoutIcon', action: 'logout'}],
      availableLanguages: [
        {lang: 'English', value: 'en'},
        {lang: 'عربي', value: 'ar'},
      ],
    }
  },
  computed: {
    ...mapGetters({
      platformLanguage: get.PLATFORM_LANGUAGE,
    }),
    currentLanguage() {
      return this.availableLanguages.find(
        (lang) => lang.value === this.platformLanguage
      )
    },
  },
  methods: {
    capitalizeFirstLetter,
    ...mapActions([action.POST_PLATFORM_LANGUAGE]),
    updateLanguage(newLang) {
      this[action.POST_PLATFORM_LANGUAGE](newLang)
      return newLang
    },
    getIcon(value) {
      return capitalizeFirstLetter(value) + 'Icon'
    },
  },
}
</script>

<style lang="scss" scoped>
.profile-menu-wrapper {
  display: flex;
  flex-direction: column;

  padding: 8px;
  width: 280px;

  border-radius: 8px;
  background: var(--background-secondary-color);
  box-shadow: 1px 2px 6px 0px rgba(135, 135, 135, 0.25);

  .user-name {
    display: flex;
    flex-direction: column;
    align-items: center;

    margin-bottom: 16px;

    .name {
      font-size: 16px;
      font-weight: 500;
    }

    .email {
      font-size: 11px;
    }
  }

  .setting {
    display: flex;
    align-items: center;
    gap: 10px;

    padding: 8px 12px;

    cursor: pointer;

    font-size: 16px;
    color: var(---icon-primary-color);

    &:hover {
      color: var(--primary-hover-color);
    }
  }

  .laguages {
    padding: 10px 22px;
    margin: 0 -8px;

    background-color: var(--background-additional-color);

    font-size: 10px;
    font-weight: 500;
    color: var(--typography-primary-color);
  }
  .lang-item {
    display: flex;
    align-items: center;
    gap: 10px;

    padding: 10px 12px;

    cursor: pointer;

    &:hover {
      color: var(--primary-hover-color);
    }
  }

  .arrow-icon {
    margin-left: auto;

    color: var(--primary-color);
  }
}
</style>
