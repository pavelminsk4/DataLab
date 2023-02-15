<template>
  <div class="main-layout">
    <MainHeader />
    <section class="content">
      <div v-if="!isLoading" class="content__header">
        <div>
          <div v-if="backPage" class="back-button" @click="backToPage">
            <ArrowLeftIcon class="arrow-back" />
            <span>Back to {{ backPage.name }}</span>
          </div>

          <div class="title-wrapper">
            <h1 class="main-layout__title">{{ title }}</h1>
            <slot name="titles-item"></slot>
          </div>

          <div v-if="description" class="main-layout__description">
            {{ description }}
          </div>
        </div>
      </div>

      <slot></slot>
    </section>
  </div>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import ArrowLeftIcon from '@/components/icons/ArrowLeftIcon'
import MainHeader from '@components/navigation/MainHeader'

export default {
  name: 'MainLayout',
  components: {
    ArrowLeftIcon,
    MainHeader,
  },
  props: {
    isLoading: {
      type: Boolean,
      default: false,
    },
    title: {
      type: String,
      default: '',
    },
    description: {
      type: String,
      default: '',
    },
    backPage: {
      type: Object,
      default: null,
    },
  },
  created() {
    if (!this.userInfo) {
      this[action.GET_USER_INFORMATION]()
    }

    if (!this.workspaces.length) {
      this[action.GET_WORKSPACES]()
    }
  },
  computed: {
    ...mapGetters({
      workspaces: get.WORKSPACES,
      userInfo: get.USER_INFO,
    }),
  },
  methods: {
    ...mapActions([action.GET_USER_INFORMATION, action.GET_WORKSPACES]),
    backToPage() {
      this.$router.push({
        name: this.backPage.routName,
      })
    },
  },
}
</script>

<style lang="scss" scoped>
.main-layout {
  position: relative;

  padding: calc(var(--header-height) + 24px) 40px 50px 95px;
  min-height: 100%;

  &__title {
    font-weight: 700;
    font-size: 28px;
    line-height: 28px;
  }

  &__description {
    margin-top: 5px;

    color: var(--typography-secondary-color);
  }
}

.content {
  z-index: 2;

  &__header {
    display: flex;
    justify-content: space-between;

    margin-bottom: 20px;
  }
}

.back-button {
  margin-bottom: 16px;
  max-width: fit-content;

  cursor: pointer;

  color: var(--typography-secondary-color);
  font-size: 14px;

  .arrow-back {
    margin-right: 5px;
  }

  &:hover {
    color: var(--button-primary-color);
  }
}

.title-wrapper {
  display: flex;
  align-items: center;
  gap: 8px;

  margin-top: 4px;
}
</style>
