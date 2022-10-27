<template>
  <div
    :class="['search-result-card', isClippingWidget && 'search-clipping-card']"
  >
    <section class="search-info-wrapper">
      <div class="result-img">
        <BaseCheckbox
          v-if="isCheckboxClippingWidget"
          class="status-checkbox"
          :id="id"
          @change="onChange"
        />
        <img
          v-if="img !== 'None'"
          :src="img"
          :class="['img', !isCheckboxClippingWidget && 'img-margin']"
        />
        <NoImageIcon
          v-else
          :class="['default-image', !isCheckboxClippingWidget && 'img-margin']"
        />
      </div>

      <div class="search-info">
        <div
          :class="[
            sentiment === 'positive' && 'status-positive',
            sentiment === 'negative' && 'status-negative',
            'status-default',
          ]"
        >
          {{ capitalizeFirstLetter(sentiment) }}
        </div>
        <div class="title" tabindex="0">{{ title }}</div>
        <div class="description" tabindex="0">{{ summary }}</div>
        <div class="general-information">
          <div class="general-item">
            {{ source }}
          </div>
          <div class="general-item">
            {{ country }}
          </div>
          <div class="general-item">
            {{ language }}
          </div>
          <div class="general-item">
            {{ dateOfCreation(published) }}
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import BaseCheckbox from '@/components/BaseCheckbox'
import NoImageIcon from '@/components/icons/NoImageIcon'

export default {
  name: 'BaseClippingCard',
  components: {NoImageIcon, BaseCheckbox},
  props: {
    isCheckboxClippingWidget: {
      type: Boolean,
      default: false,
    },
    isClippingWidget: {
      type: Boolean,
      default: false,
    },
    title: {
      type: String,
      required: false,
    },
    summary: {
      type: String,
      required: false,
    },
    source: {
      type: String,
      required: false,
    },
    country: {
      type: String,
      required: false,
    },
    language: {
      type: String,
      required: false,
    },
    published: {
      type: String,
      required: false,
    },
    img: {
      type: String,
      required: false,
    },
    sentiment: {
      type: String,
      required: false,
    },
    id: {
      type: Number,
      required: false,
    },
  },
  methods: {
    capitalizeFirstLetter(string) {
      return string.charAt(0).toUpperCase() + string.slice(1)
    },
    dateOfCreation(date) {
      return new Date(date).toLocaleDateString('en-US', {
        month: 'long',
        day: 'numeric',
        year: 'numeric',
      })
    },
    onChange(val) {
      this.$emit('add-element', val)
    },
  },
}
</script>

<style lang="scss" scoped>
.search-result-card {
  max-width: 100%;

  margin: 0 10px 10px 0;
  padding: 12px 21px 17px 20px;

  background: var(--secondary-bg-color);
  border-radius: 10px;
  border: 1px solid var(--input-border-color);
  box-shadow: 0 4px 10px rgba(16, 16, 16, 0.25);
}

.search-clipping-card {
  border-radius: 0;
  border: none;
  box-shadow: none;
}

.search-info-wrapper {
  display: flex;

  .result-img {
    width: 71px;
    height: 71px;
    margin-right: 18px;

    .img {
      width: inherit;
    }

    .img-margin {
      margin-top: 43px;
    }

    .status-checkbox {
      color: var(--secondary-text-color);

      margin-bottom: 12px;
    }

    .default-image {
      width: 71px;
      height: 50px;
    }
  }

  .search-info {
    display: flex;
    flex-direction: column;

    overflow: hidden;

    .title {
      cursor: pointer;

      text-overflow: ellipsis;
      white-space: nowrap;
      overflow: hidden;

      margin-bottom: 10px;

      font-weight: 600;
      font-size: 16px;
      line-height: 22px;
    }

    .title:focus {
      white-space: normal;
    }

    .description {
      cursor: pointer;
      overflow: hidden;
      text-overflow: ellipsis;
      display: -webkit-box;
      -webkit-line-clamp: 3;
      -webkit-box-orient: vertical;

      font-weight: 400;
      font-size: 14px;
      line-height: 150%;
    }

    .description:focus {
      -webkit-box-orient: revert;
    }
  }
}

.general-information {
  display: flex;

  margin-top: 10px;

  .general-item {
    position: relative;

    margin-right: 20px;

    font-weight: 400;
    font-size: 10px;
    line-height: 20px;
    color: var(--secondary-text-color);

    &:not(:last-child):before {
      position: absolute;
      top: 50%;
      right: -13px;
      transform: translate(-50%, -50%);

      content: '';

      width: 4px;
      height: 4px;

      border-radius: 100%;
      background-color: var(--secondary-text-color);
    }
  }
}

.status-default {
  position: relative;

  color: var(--secondary-text-color);

  padding-left: 12px;
  margin-bottom: 12px;

  &:before {
    position: absolute;
    top: 50%;
    left: 4px;
    transform: translate(-50%, -50%);

    content: '';
    width: 6px;
    height: 6px;

    border-radius: 100%;
    background-color: var(--secondary-text-color);
  }
}

.status-positive {
  color: var(--tag-color);

  &:before {
    background-color: var(--tag-color);
  }
}

.status-negative {
  color: var(--negative-status);

  &:before {
    background-color: var(--negative-status);
  }
}
</style>
