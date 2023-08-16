<template>
  <div class="main-layout__title-block">
    <div v-if="backPage" class="main-layout__back-button" @click="backToPage">
      <ArrowLeftIcon class="main-layout__back-button_arrow-back" />
      <CustomText tag="span" :text="`Back to ${backPage.name}`" />
    </div>

    <div class="title-wrapper">
      <CustomText v-if="shouldTranslate" tag="h1" :text="title" />

      <h1 v-else class="main-layout__title">{{ title }}</h1>
      <slot></slot>
    </div>

    <CustomText v-if="shouldTranslate && description" :text="description" />
    <div v-else class="main-layout__description">
      {{ description }}
    </div>
  </div>
</template>

<script>
import CustomText from '@/components/CustomText'
import ArrowLeftIcon from '@/components/icons/ArrowLeftIcon'

export default {
  name: 'MainLayoutTitleBlock',
  components: {
    ArrowLeftIcon,
    CustomText,
  },
  props: {
    title: {type: String, default: ''},
    description: {type: String, default: ''},
    backPage: {type: Object, default: null},
    shouldTranslate: {type: Boolean, default: true},
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
