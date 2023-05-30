<template>
  <div v-if="itemsTest" class="drag-n-drop-wrapper">
    <div
      v-for="(item, index) in statuses"
      :key="'status' + index"
      :id="item.status"
      class="drop-zone"
      @drop="onDrop($event, index)"
      @dragenter="getTestEnter($event, index)"
      @dragover="getSelectArea($event, item.allowedToDarag)"
      @mousedown="getIdArea(index)"
    >
      <TFSColumnHeader
        v-model="item.page"
        :value="item.page"
        :status="item.status"
        :status-color="item.color"
        :number-of-pages="numberOfPages(item.status)"
        :number-of-results="this.itemsTest[item.status]?.count"
        @update-page="updatePage"
        @decrease-arrow="decrease(index, item.status)"
        @increase-arrow="increase(index, item.status)"
      />

      <div
        v-for="item1 in getList(item.status)"
        :key="item1.id"
        class="drag-el"
        draggable="true"
        @dragstart="startDrag($event, item1)"
      >
        <TFSPostCard
          :postDetails="item1.online_post"
          :isBack="item1.is_back"
          :cardStatus="item1.status"
          :itemId="item1.id"
          class="post-card"
          @change-status="changeStatus"
        />
      </div>
    </div>
  </div>
</template>

<script>
import TFSPostCard from '@/components/TFSPostCard'
import TFSColumnHeader from '@/components/twenty-four-seven/drag-n-drop/TFSColumnHeader'

const MIN_PAGES_NUMBER = 1

export default {
  name: 'TFSDragAndDrop',
  components: {TFSPostCard, TFSColumnHeader},
  props: {
    itemsTest: {type: Object, reqared: true},
  },
  data() {
    return {
      numberOfPage: 1,
      currentAreaId: null,
      newAreaId: null,
      statuses: [
        {
          status: 'Picking',
          page: 1,
          color: '#2A7697',
          allowedToDarag: ['Summary', 'Irrelevant'],
        },
        {
          status: 'Summary',
          page: 1,
          color: '#3746A6',
          allowedToDarag: ['Q&A Check', 'Irrelevant'],
        },
        {
          status: 'Q&A Check',
          page: 1,
          color: '#AB3E00',
          allowedToDarag: ['Summary', 'Publishing', 'Irrelevant'],
        },
        {
          status: 'Publishing',
          page: 1,
          color: '#2A8500',
          allowedToDarag: ['Published', 'Summary', 'Q&A Check', 'Irrelevant'],
        },
        {status: 'Published', page: 1, color: '#961CCF', allowedToDarag: []},
      ],
    }
  },
  methods: {
    getList(status) {
      return this.itemsTest[status]?.results
    },

    startDrag($event, item) {
      $event.dataTransfer.dropEffect = 'move'
      $event.dataTransfer.effectAllowed = 'move'
      $event.dataTransfer.setData('itemID', item.id)
    },

    onDrop($event, index) {
      this.statuses[this.currentAreaId].allowedToDarag.filter((el) => {
        // const statusId = document.getElementById(el)
        console.log(this.statuses[this.currentAreaId])
        const itemID = $event.dataTransfer.getData('itemID')
        let test12345 = document.getElementById(el)
        let isBack = index > this.currentAreaId
        test12345.style.background = ''
        if (el === this.newAreaId) {
          this.$emit(
            'update-status',
            itemID,
            this.statuses[index].status,
            this.statuses[this.currentAreaId].status,
            this.statuses[index].page,
            !isBack
          )
        }
      })
    },

    getIdArea(id) {
      this.currentAreaId = id
    },

    changeStatus(itemId, newStatus, oldStatus) {
      let newStatusIndex = this.statuses.findIndex(
        (el) => el.status === newStatus
      )
      let isBack = newStatusIndex > this.currentAreaId
      this.$emit(
        'change-status-via-dropdown',
        itemId,
        newStatus,
        oldStatus,
        this.numberOfPage,
        !isBack
      )
    },

    countResults(item) {
      return this.itemsTest[item.status]?.count
    },

    numberOfPages(status) {
      let countOfPages = Math.ceil(this.itemsTest[status]?.count / 20)
      return Array.from({length: countOfPages}, (_, i) => +i + 1)
    },

    updatePage(page, status) {
      this.$emit('update-page', page, status)
    },

    increase(index, status) {
      let countOfPages = Math.ceil(this.itemsTest[status]?.count / 20)

      if (this.statuses[index].page >= countOfPages) return

      this.statuses[index].page = +this.statuses[index].page + 1
      let newValue = this.statuses[index].page

      if (newValue >= countOfPages) return

      this.updatePage(newValue, status)
    },
    decrease(index, status) {
      if (this.statuses[index].page <= MIN_PAGES_NUMBER) return

      this.statuses[index].page -= 1
      let newValue = this.statuses[index].page

      this.updatePage(newValue, status)
    },

    async getSelectArea($event) {
      $event.preventDefault()
      await this.statuses[this.currentAreaId].allowedToDarag.filter((el) => {
        if (el === $event.target.id) {
          this.newAreaId = $event.target.id
          $event.target.style.background = '#DAF9CE'
        }
        return
      })

      // $event.target.style.background = ''
      return
    },
    getTestEnter($event) {
      $event.preventDefault()
    },
  },
}
</script>

<style lang="scss" scoped>
.drag-n-drop-wrapper {
  display: flex;

  .drop-zone {
    width: 320px;
    flex-shrink: 0;
  }
}

.drop-zone {
  width: 50%;
  margin: 50px auto;
  padding: 10px;
  min-height: 10px;
}

.drag-el {
  color: azure;
  padding: 5px;
  margin-bottom: 10px;

  .post-card {
    width: 290px;
  }
}

.drag-el:nth-last-of-type(1) {
  margin-bottom: 0;
}
</style>
