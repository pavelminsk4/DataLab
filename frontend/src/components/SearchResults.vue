<template>
  <div class="search-result-wrapper">
    <div class="filters">
      <div>{{ searchData.length }} results</div>
      <Datepicker
        v-model="selectedDate"
        @update:modelValue="handleDate"
        :clearable="false"
        :format="format"
        class="dp-wrapper"
        inputClassName="dp-custom-input"
        menuClassName="dp-custom-menu"
        calendarClassName="dp-custom-calendar"
        range
      >
        <template #input-icon>
          <CalendarIcon class="dp-icon" />
        </template>
      </Datepicker>
    </div>
    <div v-if="loading" class="spinner-wrapper"><BaseSpinner /></div>
    <div v-if="searchData.length" class="search-result-cards">
      <div
        v-for="(item, index) in searchData"
        :key="'result' + index"
        class="search-result-card"
      >
        <section class="search-info-wrapper">
          <div class="result-img">
            <BaseCheckbox class="status-checkbox" />
            <img
              v-if="item.entry_media_thumbnail_url !== 'None'"
              :src="item.entry_media_thumbnail_url"
              class="img"
            />
            <NoImageIcon v-else class="default-image" />
          </div>

          <div class="search-info">
            <div
              :class="[
                item.sentiment === 'positive' && 'status-positive',
                item.sentiment === 'negative' && 'status-negative',
                'status-default',
              ]"
            >
              {{ capitalizeFirstLetter(item.sentiment) }}
            </div>
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
    <div v-if="!searchData.length && !loading">No results.</div>
  </div>
</template>

<script>
import {mapActions, mapState} from 'vuex'
import {langCodes} from '@/lib/language-codes'

import BaseSpinner from '@/components/BaseSpinner'
import BaseCheckbox from '@/components/BaseCheckbox'
import NoImageIcon from '@/components/icons/NoImageIcon'

import Datepicker from '@vuepic/vue-datepicker'
import '@vuepic/vue-datepicker/dist/main.css'
import CalendarIcon from '@/components/icons/CalendarIcon'
import {action} from '@store/constants'

export default {
  name: 'SearchResults',
  components: {
    CalendarIcon,
    BaseCheckbox,
    BaseSpinner,
    NoImageIcon,
    Datepicker,
  },
  data() {
    return {
      selectedDate: [new Date(), new Date()],
    }
  },
  computed: {
    ...mapState(['searchData', 'loading']),
  },
  methods: {
    ...mapActions([action.UPDATE_ADDITIONAL_FILTERS]),
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
    capitalizeFirstLetter(string) {
      return string.charAt(0).toUpperCase() + string.slice(1)
    },
    handleDate(modelData) {
      try {
        this.selectedDate = modelData
        this[action.UPDATE_ADDITIONAL_FILTERS]([
          {data_range: this.selectedDate},
        ])
      } catch (e) {
        console.log(e)
      }
    },
    format(date) {
      const formattedDate = date.map((el) =>
        el.toLocaleString('en-US', {
          month: 'short',
          day: 'numeric',
          year: 'numeric',
        })
      )
      return `${formattedDate[0]} - ${formattedDate[1]}`
    },
  },
}
</script>

<style lang="scss" scoped>
.search-result-wrapper {
  display: flex;
  flex-direction: column;
  align-items: flex-start;

  width: 50%;
  margin-left: 108px;

  color: var(--primary-text-color);
}

.filters {
  display: flex;
  align-items: center;
  justify-content: space-between;

  width: 100%;
  margin-bottom: 25px;

  font-weight: 400;
  font-size: 14px;
  line-height: 20px;
  color: var(--secondary-text-color);
}

.spinner-wrapper {
  display: flex;
  align-items: center;
  justify-content: center;

  min-width: 100%;
  margin-bottom: 80px;
}

.search-result-cards {
  overflow: auto;

  height: 1000px;
  width: 100%;

  &::-webkit-scrollbar {
    height: 5px;
    width: 5px;
  }

  &::-webkit-scrollbar-track {
    background: var(--secondary-bg-color);
    border: 1px solid var(--input-border-color);
    border-radius: 10px;
  }

  &::-webkit-scrollbar-thumb {
    height: 4px;

    background: var(--secondary-text-color);
    border-radius: 10px;
  }
}

.search-result-card {
  max-width: 100%;

  margin: 0 10px 10px 0;
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

.status-checkbox {
  color: var(--secondary-text-color);

  margin-bottom: 12px;
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

.default-image {
  width: 71px;
  height: 50px;
}
</style>

<style lang="scss">
.dp-wrapper {
  width: 260px;
  max-width: 100%;
  margin-left: 37px;

  &:hover {
    border-color: var(--primary-button-color);
  }
}

.dp-icon {
  margin-left: 25px;
}

.dp-custom-input {
  padding-left: 48px;

  box-shadow: 0 4px 10px rgba(16, 16, 16, 0.25);
  border: 1px solid var(--input-border-color);
  border-radius: 8px;
  background-color: var(--secondary-bg-color);

  font-family: 'Poppins', sans-serif;
  font-weight: 400;
  font-size: 14px;
  line-height: 20px;
  color: var(--primary-text-color);

  &:hover,
  &:active {
    border-color: var(--primary-button-color);
  }
}

.dp-custom-calendar,
.dp__arrow_top {
  border: none;
  background-color: var(--secondary-bg-color);

  .dp__calendar_item,
  .dp__calendar_header_item {
    color: var(--primary-text-color);
  }

  .dp__calendar_header_separator {
    background: var(--primary-button-color);
  }

  .dp__range_between {
    border: 0;
    background-color: rgba(16, 16, 16, 0.25);
  }

  .dp__range_end,
  .dp__range_start,
  .dp__active_date {
    background-color: var(--primary-button-color);
  }
}

.dp__selection_preview {
  color: var(--primary-text-color);
}

.dp__select {
  color: var(--primary-button-color);
}

.dp__action_row,
.dp__button,
.dp__instance_calendar {
  background-color: var(--secondary-bg-color);

  .dp__month_year_row {
    color: var(--primary-text-color);
  }

  .dp__month_year_col_nav {
    color: var(--primary-text-color);
  }
}

.dp__menu {
  border-radius: 8px !important;
  border: 1px solid var(--primary-button-color) !important;

  .dp__instance_calendar {
    border-radius: 8px !important;
  }

  .dp__action_row {
    border-bottom-left-radius: 8px;
    border-bottom-right-radius: 8px;
  }
}
</style>
