<template>
  <div class="search-result-wrapper">
    <div class="filters">Filters</div>
    <div v-if="searchData.length" class="search-result-cards">
      <div
        v-for="(item, index) in searchData"
        :key="'result' + index"
        class="search-result-card"
      >
        <section class="search-info-wrapper">
          <div class="result-img">
            <BaseCheckbox class="status" />
            <img
              v-if="item.entry_media_thumbnail_url !== 'None'"
              :src="item.entry_media_thumbnail_url"
              class="img"
            />
            <NoImageIcon v-else class="no-image" />
          </div>

          <div class="search-info">
            <div class="status">Positive</div>
            <div class="title" tabindex="0">{{ item.entry_title }}</div>
            <div class="description" tabindex="0">{{ item.entry_summary }}</div>
            <div class="general-information">
              <div class="general-item">
                {{ resultLanguage(item.feed_language) }}
              </div>
              <div class="general-item">
                {{ dateOfCreation(item.entry_published) }}
              </div>
            </div>
          </div>
        </section>
      </div>
    </div>
    <div v-else>No results.</div>
  </div>
</template>

<script>
import {mapState} from 'vuex'
import {langCodes} from '@/lib/language-codes'

import NoImageIcon from '@/components/icons/NoImageIcon'
import BaseCheckbox from '@/components/BaseCheckbox'

export default {
  name: 'SearchResults',
  components: {BaseCheckbox, NoImageIcon},
  computed: {
    ...mapState(['searchData']),
  },
  methods: {
    resultLanguage(langCode) {
      for (let key in langCodes) {
        if (key === langCode) {
          return langCodes[key]
        }
      }
      return ''
    },
    dateOfCreation(date) {
      return new Date(date).toLocaleDateString('en-US', {
        month: 'long',
        day: 'numeric',
        year: 'numeric',
      })
    },
  },
}
</script>

<style lang="scss" scoped>
.search-result-wrapper {
  display: flex;
  flex-direction: column;
  align-items: flex-start;

  max-width: 50%;
  margin-left: 108px;

  color: var(--primary-text-color);
}

.filters {
  margin-bottom: 25px;
}

.search-result-cards {
  max-width: 100%;
}

.search-result-card {
  max-width: 100%;

  margin-bottom: 10px;
  padding: 12px 21px 17px 20px;

  background: var(--secondary-bg-color);
  border-radius: 10px;
  border: 1px solid var(--input-border-color);
  box-shadow: 0 4px 10px rgba(16, 16, 16, 0.25);
}

.search-info-wrapper {
  display: flex;
}

.result-img {
  width: 71px;
  height: 71px;
  margin-right: 18px;

  .img {
    width: inherit;
  }
}

.status {
  margin-bottom: 12px;
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

.general-information {
  display: flex;

  margin-top: 10px;

  .general-item {
    margin-right: 10px;

    font-weight: 400;
    font-size: 10px;
    line-height: 20px;
    color: var(--secondary-text-color);
  }
}

.no-image {
  width: 50px;
  height: 50px;
}
</style>
