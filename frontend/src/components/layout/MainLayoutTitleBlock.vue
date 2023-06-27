<template>
  <div class="main-layout__title-block">
    <div v-if="backPage" class="main-layout__back-button" @click="backToPage">
      <ArrowLeftIcon class="main-layout__back-button_arrow-back" />
      <span>Back to {{ backPage.name }}</span>
    </div>

    <div class="title-wrapper">
      <h1 class="main-layout__title">{{ title }}</h1>
      <slot></slot>
    </div>

    <div v-if="description" class="main-layout__description">
      {{ description }}
    </div>
  </div>
</template>

<script>
import ArrowLeftIcon from '@/components/icons/ArrowLeftIcon'

export default {
  name: 'MainLayoutTitleBlock',
  components: {
    ArrowLeftIcon,
  },
  props: {
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
  methods: {
    backToPage() {
      this.$router.push({
        name: this.backPage.routeName,
      })
    },
  },
}
</script>

<style lang="scss" scoped>
.main-layout {
  &__title-block {
    display: flex;
    flex-direction: column;

    margin-bottom: 20px;
  }

  &__title {
    font-weight: 700;
    font-size: 28px;
    line-height: 28px;
  }

  &__description {
    margin-top: 5px;

    color: var(--typography-secondary-color);
  }

  &__back-button {
    margin-bottom: 16px;
    max-width: fit-content;

    cursor: pointer;

    color: var(--typography-secondary-color);
    font-size: 14px;

    &_arrow-back {
      margin-right: 5px;
    }

    &:hover {
      color: var(--button-primary-color);
    }
  }
}

.title-wrapper {
  display: flex;
  align-items: center;
  gap: 8px;

  margin-top: 4px;
}
</style>
