<template>
  <div class="search-result-wrapper">
    <div class="filters">
      <div v-if="isCheckboxClippingWidget" class="clipping-wrapper">
        <BaseCheckbox />
        <ArrowDownIcon
          @click="openClippingDropdown"
          :class="['icon', isOpenClippingDropdown && 'icon-flip']"
        />

        <div v-if="isOpenClippingDropdown" class="dropdown">
          <div class="item" @click="createClippingWidget">
            <ClippingIcon /> Clipping
          </div>
        </div>
      </div>

      <div>{{ searchData.length }} results</div>

      <div class="calendar-wrapper">
        <div class="trigger-wrapper" @click="openCalendar">
          <CalendarIcon class="dp-icon" />
          <div>{{ calendarDate }}</div>
          <ArrowDownIcon :class="[isShowCalendar && 'open-calendar']" />
        </div>
        <BaseCalendar v-if="isShowCalendar" :current-project="currentProject" />
      </div>
    </div>
    <div v-if="loading" class="spinner-wrapper"><BaseSpinner /></div>

    <div v-if="searchData.length" class="search-result-cards">
      <BaseClippingCard
        v-for="(item, index) in searchData"
        :key="'result' + index"
        :img="item.entry_media_thumbnail_url"
        :sentiment="item.sentiment"
        :title="item.entry_title"
        :summary="item.entry_summary"
        :source="item.feedlink__source1"
        :country="item.feedlink__country"
        :language="item.feed_language__language"
        :published="item.entry_published"
        :id="item.id"
        :is-checkbox-clipping-widget="true"
        :clipping-element="selectedClippingElement(item.id)"
        @add-element="onChange"
      />
    </div>
    <div v-if="!loading && !searchData.length">No results.</div>
  </div>
</template>

<script>
import {mapActions, mapState} from 'vuex'
import {action} from '@store/constants'

import BaseSpinner from '@/components/BaseSpinner'
import BaseCheckbox from '@/components/BaseCheckbox'
import BaseCalendar from '@/components/datepicker/BaseCalendar'
import BaseClippingCard from '@/components/BaseClippingCard'

import CalendarIcon from '@/components/icons/CalendarIcon'
import ArrowDownIcon from '@/components/icons/ArrowDownIcon'
import ClippingIcon from '@/components/icons/ClippingIcon'

export default {
  name: 'SearchResults',
  components: {
    ClippingIcon,
    BaseCheckbox,
    BaseClippingCard,
    ArrowDownIcon,
    CalendarIcon,
    BaseCalendar,
    BaseSpinner,
  },
  props: {
    currentProject: {
      type: [Array, Object],
      required: false,
    },
    isCheckboxClippingWidget: {
      type: Boolean,
      default: false,
    },
    clippingContent: {
      type: [Array, Object],
      required: false,
    },
  },
  data() {
    return {
      isShow: false,
      isOpenClippingDropdown: false,
      clippingElements: [],
    }
  },
  created() {
    document.addEventListener('click', this.close)
  },
  computed: {
    ...mapState([
      'searchData',
      'loading',
      'additionalFilters',
      'isShowCalendar',
    ]),
    calendarDate() {
      if (this.additionalFilters?.date_range?.length) {
        const currentDate = this.additionalFilters?.date_range.map((el) =>
          this.formatDate(el)
        )

        return `${currentDate[0]} - ${currentDate[1]}`
      } else {
        return `${this.formatDate(this.getLastWeeksDate())} - ${this.formatDate(
          new Date()
        )}`
      }
    },
    clippingArray() {
      let clipping = []

      for (let el of this.clippingElements) {
        clipping.push({project: this.currentProject.id, post: el})
      }

      return clipping
    },
  },
  methods: {
    ...mapActions([
      action.REFRESH_DISPLAY_CALENDAR,
      action.DELETE_CLIPPING_FEED_CONTENT,
      action.CREATE_CLIPPING_FEED_CONTENT_WIDGET,
      action.GET_CLIPPING_FEED_CONTENT_WIDGET,
    ]),
    getLastWeeksDate() {
      const now = new Date()

      return new Date(now.getFullYear(), now.getMonth(), now.getDate() - 7)
    },
    formatDate(date) {
      return date.toLocaleString('en-US', {
        month: 'short',
        day: 'numeric',
        year: 'numeric',
      })
    },
    openCalendar() {
      if (this.isShowCalendar) {
        this.isShow = false
      } else {
        this.isShow = true
      }
      this[action.REFRESH_DISPLAY_CALENDAR](this.isShow)
    },
    close() {
      const elements = document.querySelectorAll('.calendar-wrapper')

      if (!Array.from(elements).find((el) => el.contains(event.target))) {
        this[action.REFRESH_DISPLAY_CALENDAR](false)
      }
    },
    openClippingDropdown() {
      this.isOpenClippingDropdown = !this.isOpenClippingDropdown
    },
    onChange(args) {
      const {id, checked} = args
      if (checked) {
        this.clippingElements.push(id)
      } else {
        let element = this.clippingElements.indexOf(id)
        this.removeSelectedFilter(element, id)
      }
    },
    async removeSelectedFilter(index, id) {
      await this[action.DELETE_CLIPPING_FEED_CONTENT]({
        projectId: this.currentProject.id,
        postId: id,
      })
      this.clippingElements.splice(index, 1)
      this[action.GET_CLIPPING_FEED_CONTENT_WIDGET](this.currentProject.id)
    },
    createClippingWidget() {
      this[action.CREATE_CLIPPING_FEED_CONTENT_WIDGET](this.clippingArray)
    },
    selectedClippingElement(id) {
      return this.clippingContent?.some((el) => el.post__id === id)
    },
  },
}
</script>

<style lang="scss" scoped>
.search-result-wrapper {
  display: flex;
  flex-direction: column;
  align-items: flex-start;

  width: 43vw;

  color: var(--primary-text-color);
}

.clipping-wrapper {
  position: relative;

  display: flex;
  align-items: center;
  justify-content: center;
  gap: 7px;

  margin-left: 20px;

  .icon {
    cursor: pointer;

    color: var(--primary-text-color);
  }

  .icon-flip {
    transform: rotate(180deg);
  }

  .dropdown {
    z-index: 1000;

    position: absolute;
    top: 25px;
    left: -2px;

    display: flex;

    background: var(--progress-line);
    border: 1px solid var(--modal-border-color);
    border-radius: 10px;

    font-style: normal;
    font-weight: 400;
    font-size: 12px;
    line-height: 20px;
    color: var(--primary-text-color);

    .item {
      display: flex;
      gap: 10px;

      cursor: pointer;

      padding: 9px 16px 8px;
    }

    &:hover {
      background-color: var(--primary-button-color);
    }
  }
}

.trigger-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 8px;

  max-width: 100%;
  padding: 10px 16px 10px 25px;

  background: var(--secondary-bg-color);
  border: 1px solid var(--input-border-color);
  box-shadow: 0 4px 10px rgba(16, 16, 16, 0.25);
  border-radius: 8px;

  font-style: normal;
  font-weight: 400;
  font-size: 14px;
  line-height: 20px;
  color: var(--primary-text-color);

  cursor: pointer;
}

.open-calendar {
  transform: rotate(180deg);
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

@media screen and (max-width: 1000px) {
  .search-result-wrapper {
    align-items: flex-end;
  }

  .filters {
    align-items: flex-end;
    flex-direction: column;
  }

  .search-result-card {
    margin: 0 0 10px 0;
  }
}
</style>
