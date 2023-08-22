<template>
  <div class="languages-tabs">
    <div
      v-for="(language, index) in languagesTabs"
      :key="'languages' + index"
      :class="[selectedLanguage === language && 'active-language', 'language']"
      @click="$emit('change-language', language)"
    >
      <CustomText tag="span" :text="language" />
    </div>
  </div>
</template>

<script>
import CustomText from '@/components/CustomText'

export default {
  name: 'TFSLanguagesTabs',
  components: {CustomText},
  props: {
    selectedLanguage: {type: String, required: true},
    languagesTabs: {type: Array, default: () => []},
  },
}
</script>

<style lang="scss" scoped>
.languages-tabs {
  display: flex;
  justify-content: flex-end;

  margin-bottom: 20px;

  font-weight: 500;
  font-size: 14px;

  .language {
    margin: 0 10px;

    cursor: pointer;

    &:nth-child(2) {
      position: relative;

      &::before {
        position: absolute;
        right: -10px;

        content: '';

        height: 100%;
        width: 1px;

        background-color: var(--border-color);
      }

      &::after {
        position: absolute;
        left: -10px;

        content: '';

        height: 100%;
        width: 1px;

        background-color: var(--border-color);
      }
    }
  }

  .active-language {
    border-bottom: 1px solid var(--border-active-color);

    color: var(--primary-color);
  }
}
</style>
