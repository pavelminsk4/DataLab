<template>
  <div class="wrapper">
    <component :is="stringToPascalCase(type) + 'Icon'" class="achived" />

    <div class="title">{{ type }}</div>

    <section class="information-section">
      <img :src="img" class="img" />
      <div class="source-details">
        <div class="title">{{ name }}</div>
        <div class="alias">@{{ alias }}</div>
        <div class="value">{{ value }}</div>
      </div>
    </section>

    <div class="chips">
      <slot name="chips" />
    </div>
    <slot name="sentimentBar" />
  </div>
</template>

<script>
import {stringToPascalCase} from '@/lib/utilities'
import MostActiveAuthorIcon from '@/components/icons/MostActiveAuthorIcon'
import MostInfluentialAuthorIcon from '@/components/icons/MostInfluentialAuthorIcon'

export default {
  name: 'SharingSourcesCard',
  components: {MostActiveAuthorIcon, MostInfluentialAuthorIcon},
  props: {
    type: {type: String, required: true},
    img: {type: String, required: true},
    name: {type: String, required: true},
    alias: {type: String, required: true},
    value: {type: String, required: true},
  },
  methods: {
    stringToPascalCase,
  },
}
</script>

<style lang="scss" scoped>
.wrapper {
  position: relative;

  display: flex;
  flex-direction: column;
  flex: 1;

  gap: 16px;
  height: 100%;
  padding: 16px;

  border-radius: 4px;
  background-color: var(--background-primary-color);

  .achived {
    position: absolute;
    top: 4px;
    right: 4px;
  }

  .title {
    font-style: normal;
    font-weight: 500;
    font-size: 16px;
    line-height: 20px;
    color: var(--typography-title-color);
  }

  .information-section {
    display: flex;
    gap: 8px;

    .img {
      width: 72px;
      height: 72px;

      border-radius: 36px;
    }

    .source-details {
      display: flex;
      flex-direction: column;

      .alias {
        font-weight: 400;
        font-size: 11px;
        line-height: 12px;
        color: var(--typography-title-color);
      }
      .value {
        margin-top: 12px;

        font-weight: 500;
        font-size: 18px;
        line-height: 20px;
        color: var(--typography-primary-color);
      }
    }
  }

  .chips {
    display: flex;
    gap: 8px;
    justify-self: flex-end;
  }
}
</style>
