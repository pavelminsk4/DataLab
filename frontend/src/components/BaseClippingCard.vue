<template>
  <div
    :class="[
      'search-result-card',
      isClippingWidget && 'search-clipping-card',
      clippingElement && 'clipping-card',
    ]"
  >
    <section class="search-info-wrapper">
      <div class="result-img">
        <div class="clipping-wrapper">
          <ClippingIcon
            v-if="isCheckboxClippingWidget"
            :isClippingElement="clippingElement"
            :isLoading="isLoadingClippingWidget"
            @click="addPost"
          />
          <div class="tooltip">{{ clippingTooltip }}</div>
        </div>
        <img
          v-if="img !== 'None'"
          :src="img"
          :class="['img', isCheckboxClippingWidget && 'img-margin']"
        />
        <NoImageIcon
          v-else
          :class="['default-image', isCheckboxClippingWidget && 'img-margin']"
        />
      </div>

      <div class="search-info">
        <div class="header-card">
          <div
            :class="[
              sentiment === 'positive' && 'status-positive',
              sentiment === 'negative' && 'status-negative',
              'status-default',
            ]"
          >
            {{ capitalizeFirstLetter(sentiment) }}
          </div>

          <div class="card-item">
            <PotentialReachIcon />
            {{ potentialReach }}
          </div>
        </div>
        <a
          class="title"
          id="titleCard"
          tabindex="0"
          :href="entryLink"
          target="_blank"
        >
          {{ title }}
          <OnlineIcon class="type-icon" />
        </a>

        <div class="description" tabindex="0">{{ summary }}</div>
        <div class="general-information">
          <div class="general-item">
            <SourceIcon />
            <a
              class="source-link"
              :href="'https://' + sourceLink"
              target="_blank"
            >
              {{ source }}
            </a>
          </div>
          <div class="general-item">
            <CountryIcon />
            {{ country }}
          </div>
          <div class="general-item">
            <LanguageIcon />
            {{ language }}
          </div>
          <div class="general-item">
            <CalendarIcon />
            {{ dateOfCreation(published) }}
          </div>
        </div>
      </div>
    </section>

    <CloseIcon
      v-if="isClippingWidget"
      @click="deleteClippingFeedPost"
      class="delete-clipping-feed-element"
    />
  </div>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import NoImageIcon from '@/components/icons/NoImageIcon'
import CloseIcon from '@/components/icons/CloseIcon'
import CalendarIcon from '@/components/icons/CalendarIcon'
import PotentialReachIcon from '@/components/icons/PotentialReachIcon'
import LanguageIcon from '@/components/icons/LanguageIcon'
import CountryIcon from '@/components/icons/CountryIcon'
import SourceIcon from '@/components/icons/SourceIcon'
import OnlineIcon from '@/components/icons/OnlineIcon'
import ClippingIcon from '@/components/icons/ClippingIcon'

export default {
  name: 'BaseClippingCard',
  components: {
    ClippingIcon,
    OnlineIcon,
    SourceIcon,
    CountryIcon,
    LanguageIcon,
    PotentialReachIcon,
    CalendarIcon,
    CloseIcon,
    NoImageIcon,
  },
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
    entryLink: {
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
    sourceLink: {
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
    potentialReach: {
      type: Number,
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
    postId: {
      type: Number,
      required: false,
    },
    projectId: {
      type: Number,
      required: false,
    },
    clippingElement: {
      type: Boolean,
      default: false,
    },
    currentProject: {
      type: [Array, Object],
      required: true,
    },
  },
  computed: {
    ...mapGetters({isLoading: get.LOADING_WIDGETS}),
    isLoadingClippingWidget() {
      return this.isLoading.clippingWidget
    },
    clippingTooltip() {
      return this.clippingElement
        ? 'Remove from clipping widget'
        : 'Add to clipping widget'
    },
  },
  methods: {
    ...mapActions([action.DELETE_CLIPPING_FEED_CONTENT]),
    async deleteClippingFeedPost() {
      await this[action.DELETE_CLIPPING_FEED_CONTENT]({
        projectId: this.projectId,
        postId: this.postId,
      })
    },
    capitalizeFirstLetter(string) {
      return string?.charAt(0)?.toUpperCase() + string?.slice(1)
    },
    dateOfCreation(date) {
      return new Date(date).toLocaleDateString('en-US', {
        month: 'long',
        day: 'numeric',
        year: 'numeric',
      })
    },
    addPost() {
      if (this.isLoadingClippingWidget) return
      this.$emit('add-element', this.id, this.clippingElement)
    },
  },
}
</script>

<style lang="scss" scoped>
.search-result-card {
  position: relative;

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
  border-bottom: 1px solid var(--input-border-color);
  box-shadow: none;
}

.clipping-card {
  background-color: var(--clipping-card);
}

.search-info-wrapper {
  display: flex;

  .result-img {
    width: 71px;
    height: 71px;
    margin-right: 18px;

    .clipping-wrapper {
      position: relative;
      display: flex;
      justify-content: center;

      .tooltip {
        position: absolute;
        top: -7px;
        left: 58px;
        z-index: 1;

        visibility: hidden;
        text-align: center;
        white-space: nowrap;

        padding: 10px;

        border-radius: 6px;

        background-color: var(--primary-text-color);

        font-style: normal;
        font-weight: 400;
        font-size: 14px;
        line-height: 110%;
        color: var(--secondary-button-color);

        &::after {
          content: '';

          position: absolute;
          top: 49%;
          left: -2px;
          transform: translate(-50%, -50%) rotate(225deg);

          margin-left: 2px;

          border-width: 5px;
          border-style: solid;
          border-top-right-radius: 2px;

          color: var(--primary-text-color);
        }
      }

      &:hover {
        .tooltip {
          visibility: visible;
        }
      }
    }

    .img {
      object-fit: cover;

      width: inherit;
      height: 100%;

      border-radius: 4px;
    }

    .img-margin {
      margin-top: 18px;
    }

    .default-image {
      width: 71px;
      height: 50px;
    }
  }

  .search-info {
    display: flex;
    flex-direction: column;

    width: 100%;

    overflow: hidden;

    .header-card {
      display: flex;
      justify-content: space-between;

      .card-item {
        display: flex;
        align-items: center;
        gap: 6px;

        margin-right: 20px;

        text-decoration: none;

        font-weight: 400;
        font-size: 10px;
        line-height: 20px;
        color: var(--secondary-text-color);
      }
    }

    .title {
      cursor: pointer;

      text-decoration: none;
      white-space: pre-wrap;
      margin-bottom: 10px;

      font-weight: 600;
      font-size: 16px;
      line-height: 22px;
      color: inherit;

      .type-icon {
        margin-left: 8px;

        color: var(--key-word-color);
      }
    }

    .title:hover {
      color: var(--primary-button-color);
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
  flex-wrap: wrap;

  margin-top: 10px;

  .general-item {
    position: relative;

    display: flex;
    align-items: center;
    gap: 6px;

    margin-right: 20px;

    font-weight: 400;
    font-size: 10px;
    line-height: 20px;
    color: var(--secondary-text-color);
  }

  .source-link {
    text-decoration: none;

    font-weight: 400;
    font-size: 10px;
    line-height: 20px;
    color: var(--secondary-text-color);

    &:hover {
      color: var(--primary-button-color);
    }
  }
}

.status-default {
  position: relative;

  width: 70px;
  padding: 0 12px;
  margin-bottom: 12px;

  border-radius: 5px;
  background-color: rgba(145, 152, 167, 0.2);

  font-style: normal;
  font-weight: 400;
  font-size: 12px;
  line-height: 20px;
  color: var(--secondary-text-color);
}

.delete-clipping-feed-element {
  position: absolute;
  top: 12px;
  right: 0;

  cursor: pointer;

  color: var(--secondary-text-color);
}

.status-positive {
  background-color: rgba(48, 244, 126, 0.2);

  color: var(--tag-color);
}

.status-negative {
  width: 80px;

  background-color: rgba(249, 71, 71, 0.2);

  color: var(--negative-status);
}

.keyword {
  color: var(--keyword);
}
</style>
