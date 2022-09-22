<template>
  <div class="settings-nav-wrapper">
    <div v-for="(item, index) in settings" :key="'setting' + index">
      <div class="nav-title">{{ item.name }}</div>
    </div>
  </div>
  <div class="nav-wrapper">
    <div class="title-wrapper">
      <div class="back-button" @click="backToHome">
        <ArrowLeftIcon class="arrow-back" />
        Back to Dashboard
      </div>

      <h1 class="title">{{ projectName }}</h1>

      <div class="hint">
        {{ hint }}
      </div>
    </div>
    <BaseButton class="button"><slot></slot></BaseButton>
  </div>
</template>

<script>
import {mapActions, mapState} from 'vuex'
import {action} from '@store/constants'

import BaseButton from '@components/buttons/BaseButton'

import ArrowLeftIcon from '@components/icons/ArrowLeftIcon'

export default {
  name: 'SettingsNav',
  components: {BaseButton, ArrowLeftIcon},
  props: {
    title: {
      type: String,
      default: '',
    },
    hint: {
      type: String,
      default: '',
    },
  },
  data() {
    return {
      settings: [
        {
          name: 'Analytics',
        },
        {
          name: 'Search',
        },
        {
          name: 'Alerts',
        },
        {
          name: 'Reports',
        },
        {
          name: 'Settings',
        },
      ],
    }
  },
  created() {
    if (!this.workspaces.length) {
      this[action.GET_WORKSPACES]()
    }
  },
  computed: {
    ...mapState(['workspaces']),
    workspaceId() {
      return this.$route.params.workspaceId
    },
    projectId() {
      return this.$route.params.projectId
    },
    currentWorkspace() {
      return this.workspaces.filter((el) => el.id === +this.workspaceId)
    },
    currentProject() {
      return this.currentWorkspace[0]?.projects.filter(
        (el) => el.id === +this.projectId
      )[0]
    },
    projectName() {
      return this.currentProject?.title
    },
  },
  methods: {
    ...mapActions([action.GET_WORKSPACES]),
    backToHome() {
      this.$router.push({
        name: 'Home',
      })
    },
  },
}
</script>

<style lang="scss" scoped>
.settings-nav-wrapper {
  position: absolute;
  left: 0;

  display: flex;
  align-items: center;

  width: 100%;
  height: 50px;
  padding: 0 69px 0 79px;
  margin: -28px 0 0;

  background-color: var(--primary-button-color);
}

.nav-title {
  margin-right: 34px;

  font-style: normal;
  font-weight: 400;
  font-size: 14px;
  line-height: 22px;

  color: #ffffff;
}

.nav-wrapper {
  display: flex;
  justify-content: space-between;
  align-items: center;

  margin: 80px 0 50px;
}

.title-wrapper {
  display: flex;
  flex-direction: column;
}

.back-button {
  cursor: pointer;

  margin-bottom: 10px;

  font-style: normal;
  font-weight: 400;
  font-size: 14px;
  line-height: 20px;
  color: var(--primary-button-color);

  .arrow-back {
    margin-right: 6px;
  }
}

.title {
  margin-bottom: 6px;

  font-style: normal;
  font-weight: 600;
  font-size: 36px;
  line-height: 54px;
  color: var(--primary-text-color);
}

.hint {
  font-style: normal;
  font-weight: 400;
  font-size: 14px;
  line-height: 20px;
  color: var(--secondary-text-color);
}

.button {
  width: 117px;
}
</style>
